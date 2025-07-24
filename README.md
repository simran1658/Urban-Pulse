# 🏙️ Urban Pulse

## 🚦 Intelligent Traffic Signal System

Urban Pulse is an **AI-powered traffic signal management system** that uses **YOLOv5 for vehicle detection** and **real-time lane density analysis**, simulating smart traffic lights for efficient traffic flow management.

---

### ✨ Features

- 🚗 **Vehicle Detection:** Uses YOLOv5 to detect and count vehicles in each lane.
- 📈 **Real-Time Lane Density Analysis:** Calculates vehicle density to determine congestion levels.
- ⏱️ **Dynamic Signal Timing:** Adjusts traffic light durations based on lane density to reduce congestion.
- 🎮 **Simulation:** Displays smart traffic signal simulation using PyGame.

---

### 🛠️ Tech Stack

- 🐍 **Python**
- 🔍 **YOLOv5** – object detection
- 📷 **OpenCV** – video frame processing
- ➗ **NumPy** – numerical operations
- 🕹️ **PyGame** – simulation interface

---

### ⚙️ How It Works

1. 🎥 **Input:** Video stream or camera feed of an intersection.
2. 🔎 **Detection:** YOLOv5 detects vehicles in each lane.
3. 📊 **Density Analysis:** Calculates the number of vehicles per lane.
4. 🚦 **Signal Timing:** Dynamically adjusts green light time based on density.
5. 🖥️ **Simulation:** Displays signal changes and vehicle flow using PyGame.

---
