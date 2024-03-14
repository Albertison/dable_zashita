from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id = StringField('id астронафта', validators=[DataRequired()])
    password = PasswordField('Пароль астронафта', validators=[DataRequired()])
    id_capitan = StringField('id капитана', validators=[DataRequired()])
    password_capitain = PasswordField('Пароль капитана', validators=[DataRequired()])
    klick = SubmitField('доступ')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('work.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')