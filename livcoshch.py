#!/usr/bin/env python


from flask import Flask, render_template, Response
import cv2
import socket
import io

app = Flask(__name__)


vc1 = cv2.VideoCapture(0)
#print(vc1)


@app.route('/')
def index():
    """Video streaming"""
    return render_template('index.html')

def gen1():
    """Video streaming generator function."""

    while True:

       success, frame = vc1.read()  # read the camera frame

       if not success:
           break


       else:
           ret, buffer = cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()
           yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')





@app.route('/video_feed1')
def video_feed1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen1(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run()

    
