"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm
from ..data.models import LogUser
from .forms import LogUserForm2
from ..data.models import LogUser2

blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput', methods=['GET','POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template('public/LogUser.tmpl',form=form)

@blueprint.route('/loguserinput2', methods=['GET','POST'])
def InsertLogUser2():
    form = LogUserForm2()
    if form.validate_on_submit():
        LogUser2.create(**form.data)
    return render_template('public/LogUser2.tmpl',form=form)
