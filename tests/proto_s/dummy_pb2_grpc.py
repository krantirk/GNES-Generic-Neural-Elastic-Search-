# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import dummy_pb2 as dummy__pb2

class DummyGRPCServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.dummyAPI = channel.unary_unary(
        '/dummy.DummyGRPCService/dummyAPI',
        request_serializer=dummy__pb2.Message.SerializeToString,
        response_deserializer=dummy__pb2.Message.FromString,
        )


class DummyGRPCServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def dummyAPI(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DummyGRPCServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'dummyAPI': grpc.unary_unary_rpc_method_handler(
          servicer.dummyAPI,
          request_deserializer=dummy__pb2.Message.FromString,
          response_serializer=dummy__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dummy.DummyGRPCService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
