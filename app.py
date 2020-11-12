from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_id = request.form.get('user_id')
    print('user_id')
    data_film = {
        'name':'鬼灭之刃',
        'brief':'目前全网最火的番剧之一',
        'image_url':'static/鬼灭之刃.jpeg'
    }
    return render_template("recommand.html", data=data_film)



@app.route('/')
def login():
    return render_template('login.html')


@app.route('/valide_login', methods=['POST'])
def valide_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if(username == 'gaoqiang' and password == '123456'):
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
