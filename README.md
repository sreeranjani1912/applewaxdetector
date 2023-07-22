Apple Wax Detector:
  The Apple Wax Detector is a web-based application that utilizes computer vision techniques to detect the presence of wax coating on apples. It helps consumers and quality control professionals identify whether apples have been coated with wax for preservation purposes.

Features:
  Image Upload: Users can upload images of apples through a user-friendly web interface.
  Image Processing: The uploaded images are processed using OpenCV to enhance the quality and extract relevant features.
  Wax Detection: A machine learning model trained on wax-coated and non-coated apple images is used to predict the presence of wax on the uploaded apple images.
  Result Display: The result page displays the uploaded image, along with the prediction of whether the apple has wax coating or not.
  Grayscale Value: The grayscale value of the uploaded apple image is also provided to give additional insight into the image analysis process.
  
file directory structure:
  - applewax/
  - app.py
  - templates/
    - index.html
  - static/
    - style.css

  Installation and Setup:
  Clone the repository: git clone https://github.com/your-username/applewaxdetector.git
  Install the required dependencies: pip install -r requirements.txt
  Start the Flask application: python app.py
  Access the application through your web browser at http://localhost:5000
Usage:
  Open the web application in your browser.
  Click on the "Upload Image" button and select an apple image from your device.
  Click the "Process" button to analyze the image for wax coating.
  The result page will display the uploaded image, grayscale value, and the prediction of whether the apple has wax coating or not.
Results and Performance:![image](https://github.com/sreeranjani1912/applewaxdetector/assets/138803936/146905d2-a16e-45de-9bba-e8293cded7f8)
![Screenshot 2023-07-22 141043](https://github.com/sreeranjani1912/applewaxdetector/assets/138803936/b5cfd003-0f04-4808-8f98-acef38148c07)




  The Apple Wax Detector utilizes a trained machine learning model that achieves an accuracy of 95% in detecting wax coating on apples. However, it is important to note that the accuracy may vary depending on image quality, lighting conditions, and variations in wax coatings.

Acknowledgments:
  This project is built on the Flask web framework and utilizes OpenCV for image processing. We would like to acknowledge the contributions of the open-source community for providing these powerful tools.

Contributing:
  We welcome contributions from the community! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the GitHub repository.

License:
  This project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal and commercial purposes.
