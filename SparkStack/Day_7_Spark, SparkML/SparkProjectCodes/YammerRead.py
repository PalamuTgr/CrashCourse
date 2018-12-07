import yampy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json


# Set up your credentials
client_id=''
client_secret=''

authenticator = yampy.Authenticator(client_id=MY_CLIENT_ID,
                                    client_secret=MY_CLIENT_SECRET)

redirect_uri = "http://example.com/auth/callback"
auth_url = authenticator.authorization_url(redirect_uri=redirect_uri)
	
access_token = authenticator.fetch_access_token(code)	
							
access_data = authenticator.fetch_access_data(code)

access_token = access_data.access_token.token

user_info = access_data.user
network_info = access_data.network

yammer = yampy.Yammer(access_token=access_token)
									
									
class MessageListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  yammer_stream = Stream(auth, MessageListener(c_socket))
  yammer_stream.filter(track=['soccer'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 5555                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )
  
#	Message Functions
# ---------------------------------------------------- 
# Get a list of messages
#import yampy

#yammer = yampy.Yammer(access_token=access_token)
#yammer.messages.all()
#yammer.messages.from_my_feed()
#yammer.messages.from_user(a_user)

# Post a new messages
#yammer.messages.create("Hello developers", group_id=developers_group_id,
#                       topics=["Python", "API", "Yammer"])
# Delete a message
#yammer.messages.delete(a_message)
# Like messages
#yammer.messages.like(a_message)
#yammer.messages.unlike(a_message)
  
  
  
#import yampy
#
#yammer = yampy.Yammer(access_token=access_token)

# Get a list of users
#yammer.users.all()
#yammer.users.in_group(a_group_id)

# Find a specific user
#yammer.users.find(a_user_id)
#yammer.users.find_by_email("user@example.com")

# Find the logged in user
#yammer.users.find_current()

# Create a new user
#yammer.users.create("user@example.org", full_name="John Doe")

# Update a user
#yammer.users.update(a_user, summary="An example user")

# Suspend and delete users
#yammer.users.suspend(a_user)
#yammer.users.delete(a_user)
  
  