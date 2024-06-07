import cv2

def capture_video():
    cap = cv2.VideoCapture(0)
    frames = []
    if cap.isOpened() == False:
        print("Error: No Camera")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return frames
