from flask import Flask, render_template, request, make_response, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['submit'] == 'sign_in':
            user = request.form['user']
            password = request.form['password']
            return render_template('welcome.html', result={'Name': user, 'Password': password})
        elif request.form['submit'] == 'sign_up':
            return redirect(url_for('registration'))
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        return render_template('welcome.html', result=request.form)
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
