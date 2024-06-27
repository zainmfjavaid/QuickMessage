from flask import Flask, render_template, session, request, redirect
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)
app.secret_key = '<replace_with_secret_key>'

connections = []


@app.route('/', methods=['GET', 'POST'])
def landing():
    if session.get('user'):
        return redirect('/message')
    
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            session['user'] = {'name': name}
            return redirect('/message')
    return render_template('landing.html')

@app.route('/message')
def message():
    if not session.get('user'):
        return redirect('/')
    
    return render_template('message.html', name=session['user']['name'])

@sock.route('/message-socket')
def message_socket(sock):
    # Append new socket connection to list of open connections
    connections.append(sock)
    try:
        while True:
            # Repeatedly check for incoming messages
            data = sock.receive()
            
            # Once a message has been received, broadcast it
            broadcast(data, sock)
    except Exception as e:
        print(f'Socket error: {e}')
    finally:
        # When the user shuts down the connection, remove it from the list of active connections
        connections.remove(sock)
        
def broadcast(message, sender):
    # Send the message to every connected user except the original sender
    for connected_socket in connections:
        try:
            if connected_socket != sender:
                connected_socket.send(message)
        except Exception as e:
            print(f'Broadcast error: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)