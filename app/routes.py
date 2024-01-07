from flask import Blueprint

chat = Blueprint('chat', __name__, url_prefix='/chat')

#
#   Chat API Endpoint
#
@chat.route('/')
def index():
    return 'hii'