from flask import Flask, render_template, request
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.abspath(__file__))


def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image


def is_apple_edible(grayscale_value):
    if grayscale_value < 100:
        return "Not edible"
    else:
        return "Edible"


def generate_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist.flatten()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    file = request.files['image']
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    cv2.imwrite(file_path, image)

    grayscale_image = convert_to_grayscale(image)
    grayscale_value = grayscale_image.mean()
    result = is_apple_edible(grayscale_value)
    histogram = generate_histogram(grayscale_image)

    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(histogram)), histogram)
    plt.title("Grayscale Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig('static/histogram.png')
    plt.close()

    return render_template('result.html', grayscale_value=grayscale_value, result=result, image_path='static/' + file.filename)


if __name__ == '__main__':
    app.run(debug=True)
