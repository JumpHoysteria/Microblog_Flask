from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
