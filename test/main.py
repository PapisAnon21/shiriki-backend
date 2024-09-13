import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://a:a@192.168.1.20:1935')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# import vlc
# player=vlc.MediaPlayer('rstp://a:a@192.168.1.20:1935')
# player.play()

# import cv2
# import imutils
# from imutils.video import VideoStream
# url = "rtsp://a:a@192.168.1.20:1935"
# video_stream = VideoStream(url)

# while True:
#     frame = video_stream.read()
#     if frame is None:
#         print('null')
#         continue
#     frame = imutils.resize(frame,width=1200)
#     cv2.imshow("myframetest",frame)
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break

# cv2.destroyAllWindows()
# video_stream.stop()