from flask_wtf import FlaskForm
import datetime
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class JobsForm(FlaskForm):
    team_leader = IntegerField('Капитан', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Объем работы', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    is_finished = BooleanField('Статус', validators=[DataRequired()], default=False)
