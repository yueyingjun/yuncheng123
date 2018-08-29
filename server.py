from flask import Flask,request
import cv2
import numpy as np
import re
import base64
app=Flask(__name__)
@app.route("/api/photo",methods=["GET","POST"])
def index():
    base=request.form["url"]

    print(base)

    base = re.sub("\s", "+", base)
    data = base64.b64decode(base)
    data = np.fromstring(data, np.uint8)
    img = cv2.imdecode(data, cv2.COLOR_BGR2RGB)
    width = img.shape[1]
    height = img.shape[0]
    myimg = np.zeros([height, width, 3], np.uint8);
    black = np.array([0, 0, 0])
    white = np.array([255, 255, 255])
    gray = np.array([125, 125, 125]);
    def distance(one, two):
        return np.sqrt(np.sum((one - two) * (one - two)));
    for y in range(0, height - 1):
        for x in range(0, width - 1):
            current = img[y, x, :]
            right = img[y, x + 1, :]
            down = img[y + 1, x, :]
            if distance(current, right) > 15 and distance(current, down) > 15:
                myimg[y, x, :] = black

            elif distance(current, right) <= 15 and distance(current, down) <= 15:
                myimg[y, x, :] = white
            else:
                myimg[y, x, :] = gray
    cv2.imwrite("face.jpg", myimg);
    cv2.destroyAllWindows();
    return "ok111111111111"

app.run("localhost",5000)