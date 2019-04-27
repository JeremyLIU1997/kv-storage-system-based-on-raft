# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import storage_service_pb2 as storage__service__pb2


class KeyValueStoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/kvstore.KeyValueStore/Get',
        request_serializer=storage__service__pb2.GetRequest.SerializeToString,
        response_deserializer=storage__service__pb2.GetResponse.FromString,
        )
    self.Put = channel.unary_unary(
        '/kvstore.KeyValueStore/Put',
        request_serializer=storage__service__pb2.PutRequest.SerializeToString,
        response_deserializer=storage__service__pb2.PutResponse.FromString,
        )
    self.AppendEntries = channel.unary_unary(
        '/kvstore.KeyValueStore/AppendEntries',
        request_serializer=storage__service__pb2.AppendEntriesRequest.SerializeToString,
        response_deserializer=storage__service__pb2.AppendEntriesResponse.FromString,
        )
    self.RequestVote = channel.unary_unary(
        '/kvstore.KeyValueStore/RequestVote',
        request_serializer=storage__service__pb2.RequestVoteRequest.SerializeToString,
        response_deserializer=storage__service__pb2.RequestVoteResponse.FromString,
        )


class KeyValueStoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppendEntries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RequestVote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=storage__service__pb2.GetRequest.FromString,
          response_serializer=storage__service__pb2.GetResponse.SerializeToString,
      ),
      'Put': grpc.unary_unary_rpc_method_handler(
          servicer.Put,
          request_deserializer=storage__service__pb2.PutRequest.FromString,
          response_serializer=storage__service__pb2.PutResponse.SerializeToString,
      ),
      'AppendEntries': grpc.unary_unary_rpc_method_handler(
          servicer.AppendEntries,
          request_deserializer=storage__service__pb2.AppendEntriesRequest.FromString,
          response_serializer=storage__service__pb2.AppendEntriesResponse.SerializeToString,
      ),
      'RequestVote': grpc.unary_unary_rpc_method_handler(
          servicer.RequestVote,
          request_deserializer=storage__service__pb2.RequestVoteRequest.FromString,
          response_serializer=storage__service__pb2.RequestVoteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kvstore.KeyValueStore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
