from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Length,EqualTo, Email, DataRequired, ValidationError
from MARKET.models import User


class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')


    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=30)])
    email_address = StringField(label='Email Adress', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password:', validators=[DataRequired(), Length(min=6, max=16)])
    password2 = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
     submit = SubmitField(label='Purchase Item!')
     
class SellItemForm(FlaskForm):
     submit = SubmitField(label='Sell Item!')





