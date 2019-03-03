import grpc
import json
# import grpc generated classes
import user_pb2
import user_pb2_grpc

# open grpc channel to user grpc server
channel = grpc.insecure_channel('localhost:9001')

stub = user_pb2_grpc.UserServiceStub(channel)

# create params
params = user_pb2.RequestParams(user_list=True)

response = stub.GetUserList(params)
data = []
for x in response.users:
  data.append(
    {
      "first_name":x.first_name,
      "last_name":x.last_name,
      "email":x.email,
      "age": x.age
    }
  )

print(json.dumps(data))


