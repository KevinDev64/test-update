import os
import socket
REMOTE_SERVER = "github.com"
def is_connected(hostname):
  try:
    # See if we can resolve the host name - tells us if there is
    # A DNS listening
    host = socket.gethostbyname(hostname)
    # Connect to the host - tells us if the host is actually reachable
    s = socket.create_connection((host, 443), 2)
    s.close()
    return True
  except Exception:
     pass # We ignore any errors, returning False
  return False
input("Ready to update!")

if is_connected(REMOTE_SERVER): os.system("git fetch && git pull")
else: print("No network!")

input("Done!")
