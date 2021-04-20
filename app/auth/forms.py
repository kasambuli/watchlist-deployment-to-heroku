from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('Your Email Address',validators=[Required(),Email()])
  username = StringField('Enter your Username',validators=[Required()])
  password = PasswordField('Password',validators=[Required(),EqualTo('confirm password',
  message='Password must match')])
  password_confirm = PasswordField('Confirm Passwords',validators=[Required()])
  submit = SubmitField('Sign up')