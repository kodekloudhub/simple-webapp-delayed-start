from flask import Flask
from flask import render_template, request
import socket
import os
import time

app = Flask(__name__)

# Get start delay from Environment variable
DELAY_FROM_ENV = os.environ.get('APP_START_DELAY') or 0
FROZEN = False


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route("/")
def main():
    if not FROZEN:
        # return 'Hello'
        return render_template('hello.html', name=socket.gethostname(), color='#16a085')


@app.route("/hostname")
def hostname():
    if not FROZEN:
        return socket.gethostname()


@app.route("/ready")
def ready():
    if not FROZEN:
        return "Message from {0} : I am ready!".format(socket.gethostname())


@app.route("/live")
def live():
    if not FROZEN:
        return "Message from {0} : I am live!".format(socket.gethostname())


@app.route("/crash")
def crash():
    shutdown_server()
    print("Message from {0} : Mayday! Mayday! Going to crash!".format(socket.gethostname()))
    return "Message from {0} : Mayday! Mayday! Going to crash!".format(socket.gethostname())


@app.route("/freeze")
def freeze():
    global FROZEN
    FROZEN = True
    while True:
        print("Message from {0} : Bad Code! I am stuck!".format(socket.gethostname()))
        time.sleep(2)


if __name__ == "__main__":

    if DELAY_FROM_ENV:
        print("Warming Up Application. Will take {0} seconds to finish.".format(DELAY_FROM_ENV))
        time.sleep(int(DELAY_FROM_ENV))

    print("Application Ready!")
    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)