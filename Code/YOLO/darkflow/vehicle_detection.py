# import cv2
# from darkflow.net.build import  TFNet
# import matplotlib.pyplot as plt 
# import os

# options={
#    'model':'./cfg/yolo.cfg',        #specifying the path of model
#    'load':'./bin/yolov2.weights',   #weights
#    'threshold':0.3                  #minimum confidence factor to create a box, greater than 0.3 good
# }

# tfnet=TFNet(options)
# inputPath = os.getcwd() + "/test_images/"
# outputPath = os.getcwd() + "/output_images/"

# def detectVehicles(filename):
#    global tfnet, inputPath, outputPath
#    img=cv2.imread(inputPath+filename,cv2.IMREAD_COLOR)
#    # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#    result=tfnet.return_predict(img)
#    print("Result of vehicle count is ",result)
#    for vehicle in result:
#       label=vehicle['label']   #extracting label
#       if(label=="car" or label=="bus" or label=="bike" or label=="truck" or label=="rickshaw"):    # drawing box and writing label
#          top_left=(vehicle['topleft']['x'],vehicle['topleft']['y'])
#          bottom_right=(vehicle['bottomright']['x'],vehicle['bottomright']['y'])
#          img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)    #green box of width 5
#          img=cv2.putText(img,label,top_left,cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)   #image, label, position, font, font scale, colour: black, line width      
#    outputFilename = outputPath + "output_" +filename
#    cv2.imwrite(outputFilename,img)
#    print('Output image stored at:', outputFilename)
#    # plt.imshow(img)
#    # plt.show()
#    # return result

# for filename in os.listdir(inputPath):
#    if(filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg")):
#       detectVehicles(filename)
# print("Done!")





import cv2
from darkflow.net.build import TFNet
import os
import json

options = {
   'model': './cfg/yolo.cfg',
   'load': './bin/yolov2.weights',
   'threshold': 0.3
}

tfnet = TFNet(options)

inputPath = os.getcwd() + "/test_images/"
outputPath = os.getcwd() + "/output_images/"

def detectVehicles(filename):
    global tfnet, inputPath, outputPath

    img = cv2.imread(inputPath + filename, cv2.IMREAD_COLOR)
    if img is None:
        print("Error: Image not found ->", inputPath + filename)
        return {}

    result = tfnet.return_predict(img)

    counts = {"car":0, "bus":0, "bike":0, "truck":0, "rickshaw":0}

    for vehicle in result:
        label = vehicle['label']
        if label in counts:
            counts[label] += 1

            top_left = (vehicle['topleft']['x'], vehicle['topleft']['y'])
            bottom_right = (vehicle['bottomright']['x'], vehicle['bottomright']['y'])
            img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 3)
            img = cv2.putText(img, label, top_left, 
                              cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    outputFilename = outputPath + "output_" + filename
    cv2.imwrite(outputFilename, img)

    print(json.dumps(counts, indent=4))
    print("Output saved at:", outputFilename)

    return counts


if __name__ == "__main__":
    print("Vehicle detection module ready.")

    test_file = "car.jpg"   # change to your actual image
    detectVehicles(test_file)

