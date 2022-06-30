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


from flask import Flask, redirect, render_template, url_for, request, send_file
from io import BytesIO, StringIO
from PIL import Image
import semana1

app = Flask(__name__)

@app.route('/get_image')
def serve_pil_image():
    img_io = BytesIO()
    pil_img = semana1.shit()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')



@app.route('/', methods=['GET','POST'])
def main():

    if request.method == 'POST':
        image = request.form['image']
        image_variable= serve_pil_image()
    else:
        serve_pil_image


    return render_template('index.html')





if __name__ == "__main__":
    app.run(debug=False)
