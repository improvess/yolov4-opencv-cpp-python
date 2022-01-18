# yolov4-opencv-cpp-python

Example of performing inference with Darknet YOLO V4, OpenCV 4.4.0 DNN, C++ and Python 

Looking for YOLO V5 OpenCV C++/Python inference? [Check this repository](https://github.com/doleron/yolov5-opencv-cpp-python)

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

If your machine/OpenCV install are CUDA capable you can try out running using the GPU:

```bash
git clone https://github.com/doleron/yolov4-opencv-cpp-python.git
cd yolov4-opencv-cpp-python
python python/yolo.py cuda
```

## Running the C++ program

The C++ code is [here](cpp/yolo.cpp).

```bash
git clone https://github.com/doleron/yolov4-opencv-cpp-python.git
cd yolov4-opencv-cpp-python
g++ -O3 cpp/yolo.cpp -o yolo_example `pkg-config --cflags --libs opencv4`
./yolo_example
```

Or using CUDA if available:

```bash
git clone https://github.com/doleron/yolov4-opencv-cpp-python.git
cd yolov4-opencv-cpp-python
g++ -O3 cpp/yolo.cpp -o yolo_example `pkg-config --cflags --libs opencv4`
./yolo_example cuda
```
![running the examples](https://github.com/doleron/yolov4-opencv-cpp-python/raw/main/yolov4.png)

PS.: Video sample from [https://www.youtube.com/watch?v=NyLF8nHIquM](https://www.youtube.com/watch?v=NyLF8nHIquM)

## Which YOLO version should I use?

This repository uses YOLO V4 but it is not the only YOLO version out there. You can read [this article](https://towardsdatascience.com/yolo-v4-or-yolo-v5-or-pp-yolo-dad8e40f7109) to learn more about YOLO versions and choose the more suitable one for you.
