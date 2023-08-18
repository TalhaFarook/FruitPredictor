from flask import Flask, request, jsonify, render_template
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__, static_folder='static')

model = tf.keras.models.load_model('fruit_classification_model.h5')
class_names = ['apple', 'banana', 'orange', 'pineapple', 'watermelon']

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        img = image.load_img(file_path, target_size=(100, 100))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Predict the class label for the image
        single_image_pred = model.predict(img_array)
        single_image_class = np.argmax(single_image_pred, axis=-1)
        predicted_class_name = class_names[single_image_class[0]]
        os.remove(file_path)

        return jsonify({"fruit": predicted_class_name})

    return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)