import grpc
from concurrent import futures
import time

#import grpc generated class
import user_pb2
import user_pb2_grpc

#import user domain
import domain as user

class UserService(user_pb2_grpc.UserServiceServicer):
  def GetUserList(self, req, ctx):
    # if req.user_list === True:
    #   return user_pb2.Empty()
    print(req.user_list)
    if not req.user_list:
      return user_pb2.Empty()
    usr_list = []
    for usr in user.get_user_list():
      usr_list.append(user_pb2.User(first_name=usr['first_name'],last_name=usr['last_name'],email=usr['email'],age=usr['age']))
    res = user_pb2.UserList(users=usr_list)

    return res
    

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

user_pb2_grpc.add_UserServiceServicer_to_server(UserService(),server)

print('User Service Server is listening on port 9001')
server.add_insecure_port('[::]:9001')
server.start()

try:
  while True:
    time.sleep(60*60*24*30)
except KeyboardInterrupt:
  server.stop(0)
