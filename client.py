import grpc

# import grpc generated classes
import user_pb2
import user_pb2_grpc

# open grpc channel to user grpc server
channel = grpc.insecure_channel('localhost:9001')

stub = user_pb2_grpc.UserServiceStub(channel)

# create params
params = user_pb2.RequestParams(user_list=True)

response = stub.GetUserList(params)

print( len(response.users))

# print(response)



