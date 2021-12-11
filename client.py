import socket as sock;

class client:
  def __init__(self, ip, port):
    self.target = { # The target server that we want to connect to.
      "ip": ip,
      "port": port
    };

    self.client = sock.socket(sock.AF_INET, sock.SOCK_STREAM);
    TryToConnect = self.connectToServer();
    if(TryToConnect["Connection?"] == True):
      self.response();
    else:
      print("Could not connect.");
    
    self.client.close();
  
  def connectToServer(self) -> dict:
    try:
      self.client.connect((self.target["ip"], self.target["port"]));
      self.client.send(b"GET / HTTP/1.1 \r\nLook at this: https://me.saatvikk.repl.co/home");
    except Exception as e:
      return {"Connection?": False, "error": e};
    
    return {"Connection?": True};
  
  def response(self):
    res = self.client.recv(4094);
    print(res.decode());


if(__name__ == "__main__"):
  NewClient = client("127.0.0.1", 9998);
