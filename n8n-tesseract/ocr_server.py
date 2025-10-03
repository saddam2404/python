from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import base64
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        data = request.get_json()

        if not data or 'image' not in data:
            return jsonify({'error': 'No image uploaded'}), 400

        print("[DEBUG] Received base64 image")  # Debug log

        # Decode base64 to bytes
        image_data = base64.b64decode(data['image'])

        # Convert bytes to image
        image = Image.open(io.BytesIO(image_data))

        # Run OCR
        text = pytesseract.image_to_string(image)

        return jsonify({'text': text})

    except Exception as e:
        print("[ERROR]", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

