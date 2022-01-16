# yolov4-opencv-cpp-python
Example of using YOLO v4 with OpenCV, C++ and Python

## Prerequisites

Make sure you have already on your system:

- OpenCV 4.0+
- Python 3.7+
- Any modern Linux OS (tested on Ubuntu 20.04)
- GCC 9.0+

## Running the python script

The python code is [here](python/yolo.py).

```bash
git clone https://github.com/doleron/yolov4-opencv-cpp-python.git
cd yolov4-opencv-cpp-python
python python/yolo.py 
```
## Running the C++ program

The C++ code is [here](cpp/yolo.cpp).

```bash
git clone https://github.com/doleron/yolov4-opencv-cpp-python.git
cd yolov4-opencv-cpp-python
g++ -O2 cpp/yolo.cpp -o yolo_example `pkg-config --cflags --libs opencv4`
./yolo_example
```
![running the examples](https://github.com/doleron/yolov4-opencv-cpp-python/raw/main/yolov4.png)
