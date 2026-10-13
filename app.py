
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('registration.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    course = request.form.get('course', '')

    return render_template(
        'success.html',
        name=username,
        email=email,
        phone=phone,
        course=course
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
