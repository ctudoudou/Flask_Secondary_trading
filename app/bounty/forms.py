from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User, Bountyissue

class BountyForm(FlaskForm):
    name = StringField('目标商品',
                        validators=[Required(), Length(1, 64),])
    introduction = TextAreaField('目标细节')
    price = StringField('悬赏金')
    submit = SubmitField('发布')