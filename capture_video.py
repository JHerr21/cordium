import cv2

# added comment

def capture_video():
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print("Error: Camera not opened")

    size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'),10, size)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('f'):
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
