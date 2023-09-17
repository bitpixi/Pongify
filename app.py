from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from pongify import pingpong_video  # importing the function from pongify.py

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded.'
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], "pong_" + filename)
    pingpong_video(filepath, output_path)

    return send_from_directory(app.config['UPLOAD_FOLDER'], "pong_" + filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
