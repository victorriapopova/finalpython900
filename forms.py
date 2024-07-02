from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=140)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Service')

class ReviewForm(FlaskForm):
    user_name = StringField('Your Name', validators=[DataRequired(), Length(max=64)])
    rating = IntegerField('Rating (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit Review')
