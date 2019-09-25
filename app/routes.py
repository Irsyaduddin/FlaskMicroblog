from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Rai'}
    posts = [
        {
            'author':{'username':'Megumin'},
            'body':'Explosion magic is a high tier magic. Fight me'
        },
        {
            'author':{'username':'YunYun'},
            'body':'I don\'t think that Explosion magic is the best type of magic.'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)

@app.route('/test')
def test():
    return render_template('test.html', title='What chu snooping for?')

