from ultralytics import YOLO

modelo = YOLO('yolo11n.pt')

modelo.predict('exemplo2.mp4',show=True)