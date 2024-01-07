from flask import request
from flask_socketio import emit
from .extensions import socketio

users = {}

@socketio.on('connect')
def handle_connect():
    print('Client has connected.')

@socketio.on('user_join')
def handle_user_join(username):
    print(f'User {username} has joined the chatroom.')
    users[username] = request.sid

@socketio.on('new_message')
def handle_new_message(message):
    username = None
    
    for user in users:
        if users[user] == request.sid:
            username = user

    emit('chat', {'username': username, 'message': message}, broadcast=True)
