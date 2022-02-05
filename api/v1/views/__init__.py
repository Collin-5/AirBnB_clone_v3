from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

"""import storage engine and classes"""
from models import storage
from models.state import State
from models.city import City

"""import flask views"""
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
