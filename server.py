import socket as sock;
import threading as thread;

class server:
  def __init__(self, ip, port) -> None:
    self.host = {
      "ip": ip,
      "port": port
    };

    self.server = self.initServer();
    self.serverListen();
    return None;

  def initServer(self):
    server = sock.socket(sock.AF_INET, sock.SOCK_STREAM);
    server.bind((self.host["ip"], self.host["port"]));
    return server;
  
  def serverListen(self):
    self.server.listen(5);
    print(f'> Listening on {self.host["ip"]}:{self.host["port"]}');

    while(True):
      client, address = self.server.accept();
      print(f'> Accepted connection from {address[0]}:{address[1]}');
      NewClient = thread.Thread(target = self.clientHandler, args = (client, address));
      NewClient.start();
  
  def clientHandler(self, socket, address):
    request = socket.recv(1024);
    print(f'> Recieved: {request.decode("utf-8")} from {address[0]}:{address[1]}');
    socket.send(b'ACK');

if(__name__ == "__main__"):
  NewServer = server("0.0.0.0", 9998);


