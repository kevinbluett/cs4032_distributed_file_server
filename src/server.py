import asyncore, sys, socket
from async.server import *
from threaded.server import *
from helpers import *

def sercurity_server_handler(server, (sock, addr)):
    data = LithiumHelper.recv_all(sock)
    data = data.replace("\r", "")
    
    if data == "KILL_SERVICE\n":
        if server is not None:
            Thread(target=server.shutdown, args=[False]).start()
    else:
        sock.send("%s\nStudentID:11311101" % (data))

    # Kill the socket
    sock.close()
    server.count.decr()

def start_server():
    # Start the server in thread pool mode
    LithiumAsyncServer('localhost', int(sys.argv[1]), sercurity_server_handler)
    asyncore.loop()

if __name__ == '__main__':
    start_server()