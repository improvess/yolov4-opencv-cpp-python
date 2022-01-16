import cv2
import time

def build_model(is_cuda):
    net = cv2.dnn.readNet("config_files/yolov4-tiny.weights", "config_files/yolov4-tiny.cfg")
    if is_cuda:
        print("Attempty to use CUDA")
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
    else:
        print("Running on CPU")
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1./255, swapRB=True)
    return model

def load_capture():
    capture = cv2.VideoCapture("sample.mp4")
    return capture

def load_classes():
    class_list = []
    with open("config_files/classes.txt", "r") as f:
        class_list = [cname.strip() for cname in f.readlines()]
    return class_list

colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]

model = build_model(True)
capture = load_capture()
class_list = load_classes()

start = time.time_ns()
frame_count = 0
total_frames = 0
fps = -1

while True:

    _, frame = capture.read()
    if frame is None:
        print("End of stream")
        break

    classIds, confidences, boxes = model.detect(frame, .2, .4)
    frame_count += 1
    total_frames += 1

    for (classid, confidence, box) in zip(classIds, confidences, boxes):
        color = colors[int(classid) % len(colors)]
        cv2.rectangle(frame, box, color, 2)
        cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), color, -1)
        cv2.putText(frame, class_list[classid[0]], (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0))

    if frame_count >= 30:
        end = time.time_ns()
        fps = 1000000000 * frame_count / (end - start)
        frame_count = 0
        start = time.time_ns()
    
    if fps > 0:
        fps_label = "FPS: %.2f" % fps
        cv2.putText(frame, fps_label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("output", frame)

    if cv2.waitKey(1) > -1:
        print("finished by user")
        break