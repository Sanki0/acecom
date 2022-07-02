# from tkinter import Image
# from flask import Flask, redirect, render_template, url_for, request, send_file
# from io import StringIO
# from PIL import Image
# import semana1

# app = Flask(__name__)


# @app.route('/success/<name>')
# def success(name):

#     return semana1.shit()

# def serve_pil_image():
#     img_io = StringIO()
#     pil_img=semana1.shit()
#     pil_img.save(img_io, 'PNG', quality=70)
#     img_io.seek(0)
#     return send_file(img_io, mimetype='image/png')


# @app.route('/', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['image']
#         return serve_pil_image()
#     else:
#         user = request.args.get('image')
#         return redirect(url_for('success', name=user))


# if __name__ == '__main__':
#     app.run()


from flask import Flask, redirect, render_template, url_for, request, send_file, flash
from io import BytesIO, StringIO
from PIL import Image
import semana1


import os
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads/'
UPLOAD_PROCESS_FOLDER='static/processed/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PROCESS_FOLDER']=UPLOAD_PROCESS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def main():
    return render_template('index.html')
    
# @app.route('/', methods=['GET','POST'])
# def upload_image():

#     if request.method == 'POST':
#         image = request.form['image']
#         image_variable= serve_pil_image()
#     else:
#         serve_pil_image()


#     return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 


@app.route('/pil/<filename>')
def serve_pil_image(filename):
    img_io = BytesIO()
    pil_img = semana1.shit(filename)
    pil_img.save(os.path.join(app.config['UPLOAD_PROCESS_FOLDER'], filename))
    print(pil_img)
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')









if __name__ == "__main__":
    app.run(debug=False)
