# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/prediction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/prediction.proto',
  package='seldon.protos',
  syntax='proto3',
  serialized_options=_b('\n\020io.seldon.protosB\020PredictionProtos'),
  serialized_pb=_b('\n\x16proto/prediction.proto\x12\rseldon.protos\x1a\x1cgoogle/protobuf/struct.proto\x1a&tensorflow/core/framework/tensor.proto\"\xb9\x01\n\rSeldonMessage\x12%\n\x06status\x18\x01 \x01(\x0b\x32\x15.seldon.protos.Status\x12!\n\x04meta\x18\x02 \x01(\x0b\x32\x13.seldon.protos.Meta\x12*\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.seldon.protos.DefaultDataH\x00\x12\x11\n\x07\x62inData\x18\x04 \x01(\x0cH\x00\x12\x11\n\x07strData\x18\x05 \x01(\tH\x00\x42\x0c\n\ndata_oneof\"\xaf\x01\n\x0b\x44\x65\x66\x61ultData\x12\r\n\x05names\x18\x01 \x03(\t\x12\'\n\x06tensor\x18\x02 \x01(\x0b\x32\x15.seldon.protos.TensorH\x00\x12-\n\x07ndarray\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00\x12+\n\x08tftensor\x18\x04 \x01(\x0b\x32\x17.tensorflow.TensorProtoH\x00\x42\x0c\n\ndata_oneof\"/\n\x06Tensor\x12\x11\n\x05shape\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x12\n\x06values\x18\x02 \x03(\x01\x42\x02\x10\x01\"\x80\x03\n\x04Meta\x12\x0c\n\x04puid\x18\x01 \x01(\t\x12+\n\x04tags\x18\x02 \x03(\x0b\x32\x1d.seldon.protos.Meta.TagsEntry\x12\x31\n\x07routing\x18\x03 \x03(\x0b\x32 .seldon.protos.Meta.RoutingEntry\x12\x39\n\x0brequestPath\x18\x04 \x03(\x0b\x32$.seldon.protos.Meta.RequestPathEntry\x12&\n\x07metrics\x18\x05 \x03(\x0b\x32\x15.seldon.protos.Metric\x1a\x43\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\x1a.\n\x0cRoutingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x32\n\x10RequestPathEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe1\x01\n\x06Metric\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .seldon.protos.Metric.MetricType\x12\r\n\x05value\x18\x03 \x01(\x02\x12-\n\x04tags\x18\x04 \x03(\x0b\x32\x1f.seldon.protos.Metric.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\nMetricType\x12\x0b\n\x07\x43OUNTER\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\t\n\x05TIMER\x10\x02\"I\n\x11SeldonMessageList\x12\x34\n\x0eseldonMessages\x18\x01 \x03(\x0b\x32\x1c.seldon.protos.SeldonMessage\"\x8e\x01\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x30\n\x06status\x18\x04 \x01(\x0e\x32 .seldon.protos.Status.StatusFlag\"&\n\nStatusFlag\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\"\xa6\x01\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12-\n\x07request\x18\x01 \x01(\x0b\x32\x1c.seldon.protos.SeldonMessage\x12.\n\x08response\x18\x02 \x01(\x0b\x32\x1c.seldon.protos.SeldonMessage\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12+\n\x05truth\x18\x04 \x01(\x0b\x32\x1c.seldon.protos.SeldonMessage\"p\n\x0fRequestResponse\x12-\n\x07request\x18\x01 \x01(\x0b\x32\x1c.seldon.protos.SeldonMessage\x12.\n\x08response\x18\x02 \x01(\x0b\x32\x1c.seldon.protos.SeldonMessage2\x89\x03\n\x07Generic\x12N\n\x0eTransformInput\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12O\n\x0fTransformOutput\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12\x45\n\x05Route\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12M\n\tAggregate\x12 .seldon.protos.SeldonMessageList\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12G\n\x0cSendFeedback\x12\x17.seldon.protos.Feedback\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32\x99\x01\n\x05Model\x12G\n\x07Predict\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12G\n\x0cSendFeedback\x12\x17.seldon.protos.Feedback\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32\x98\x01\n\x06Router\x12\x45\n\x05Route\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12G\n\x0cSendFeedback\x12\x17.seldon.protos.Feedback\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32]\n\x0bTransformer\x12N\n\x0eTransformInput\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32\x64\n\x11OutputTransformer\x12O\n\x0fTransformOutput\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32Y\n\x08\x43ombiner\x12M\n\tAggregate\x12 .seldon.protos.SeldonMessageList\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x32\x9a\x01\n\x06Seldon\x12G\n\x07Predict\x12\x1c.seldon.protos.SeldonMessage\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x12G\n\x0cSendFeedback\x12\x17.seldon.protos.Feedback\x1a\x1c.seldon.protos.SeldonMessage\"\x00\x42$\n\x10io.seldon.protosB\x10PredictionProtosb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,])



_METRIC_METRICTYPE = _descriptor.EnumDescriptor(
  name='MetricType',
  full_name='seldon.protos.Metric.MetricType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COUNTER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1092,
  serialized_end=1139,
)
_sym_db.RegisterEnumDescriptor(_METRIC_METRICTYPE)

_STATUS_STATUSFLAG = _descriptor.EnumDescriptor(
  name='StatusFlag',
  full_name='seldon.protos.Status.StatusFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1321,
  serialized_end=1359,
)
_sym_db.RegisterEnumDescriptor(_STATUS_STATUSFLAG)


_SELDONMESSAGE = _descriptor.Descriptor(
  name='SeldonMessage',
  full_name='seldon.protos.SeldonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='seldon.protos.SeldonMessage.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='seldon.protos.SeldonMessage.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='seldon.protos.SeldonMessage.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binData', full_name='seldon.protos.SeldonMessage.binData', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strData', full_name='seldon.protos.SeldonMessage.strData', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data_oneof', full_name='seldon.protos.SeldonMessage.data_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=112,
  serialized_end=297,
)


_DEFAULTDATA = _descriptor.Descriptor(
  name='DefaultData',
  full_name='seldon.protos.DefaultData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='seldon.protos.DefaultData.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='seldon.protos.DefaultData.tensor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ndarray', full_name='seldon.protos.DefaultData.ndarray', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tftensor', full_name='seldon.protos.DefaultData.tftensor', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data_oneof', full_name='seldon.protos.DefaultData.data_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=300,
  serialized_end=475,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='seldon.protos.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='seldon.protos.Tensor.shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='seldon.protos.Tensor.values', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=524,
)


_META_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='seldon.protos.Meta.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seldon.protos.Meta.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='seldon.protos.Meta.TagsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=811,
)

_META_ROUTINGENTRY = _descriptor.Descriptor(
  name='RoutingEntry',
  full_name='seldon.protos.Meta.RoutingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seldon.protos.Meta.RoutingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='seldon.protos.Meta.RoutingEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=813,
  serialized_end=859,
)

_META_REQUESTPATHENTRY = _descriptor.Descriptor(
  name='RequestPathEntry',
  full_name='seldon.protos.Meta.RequestPathEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seldon.protos.Meta.RequestPathEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='seldon.protos.Meta.RequestPathEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=861,
  serialized_end=911,
)

_META = _descriptor.Descriptor(
  name='Meta',
  full_name='seldon.protos.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='puid', full_name='seldon.protos.Meta.puid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='seldon.protos.Meta.tags', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routing', full_name='seldon.protos.Meta.routing', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestPath', full_name='seldon.protos.Meta.requestPath', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='seldon.protos.Meta.metrics', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_META_TAGSENTRY, _META_ROUTINGENTRY, _META_REQUESTPATHENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=911,
)


_METRIC_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='seldon.protos.Metric.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seldon.protos.Metric.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='seldon.protos.Metric.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1047,
  serialized_end=1090,
)

_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='seldon.protos.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seldon.protos.Metric.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='seldon.protos.Metric.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='seldon.protos.Metric.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='seldon.protos.Metric.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METRIC_TAGSENTRY, ],
  enum_types=[
    _METRIC_METRICTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=914,
  serialized_end=1139,
)


_SELDONMESSAGELIST = _descriptor.Descriptor(
  name='SeldonMessageList',
  full_name='seldon.protos.SeldonMessageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seldonMessages', full_name='seldon.protos.SeldonMessageList.seldonMessages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1141,
  serialized_end=1214,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='seldon.protos.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='seldon.protos.Status.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='seldon.protos.Status.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='seldon.protos.Status.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='seldon.protos.Status.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_STATUSFLAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1217,
  serialized_end=1359,
)


_FEEDBACK = _descriptor.Descriptor(
  name='Feedback',
  full_name='seldon.protos.Feedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='seldon.protos.Feedback.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='seldon.protos.Feedback.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='seldon.protos.Feedback.reward', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truth', full_name='seldon.protos.Feedback.truth', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1362,
  serialized_end=1528,
)


_REQUESTRESPONSE = _descriptor.Descriptor(
  name='RequestResponse',
  full_name='seldon.protos.RequestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='seldon.protos.RequestResponse.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='seldon.protos.RequestResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1530,
  serialized_end=1642,
)

_SELDONMESSAGE.fields_by_name['status'].message_type = _STATUS
_SELDONMESSAGE.fields_by_name['meta'].message_type = _META
_SELDONMESSAGE.fields_by_name['data'].message_type = _DEFAULTDATA
_SELDONMESSAGE.oneofs_by_name['data_oneof'].fields.append(
  _SELDONMESSAGE.fields_by_name['data'])
_SELDONMESSAGE.fields_by_name['data'].containing_oneof = _SELDONMESSAGE.oneofs_by_name['data_oneof']
_SELDONMESSAGE.oneofs_by_name['data_oneof'].fields.append(
  _SELDONMESSAGE.fields_by_name['binData'])
_SELDONMESSAGE.fields_by_name['binData'].containing_oneof = _SELDONMESSAGE.oneofs_by_name['data_oneof']
_SELDONMESSAGE.oneofs_by_name['data_oneof'].fields.append(
  _SELDONMESSAGE.fields_by_name['strData'])
_SELDONMESSAGE.fields_by_name['strData'].containing_oneof = _SELDONMESSAGE.oneofs_by_name['data_oneof']
_DEFAULTDATA.fields_by_name['tensor'].message_type = _TENSOR
_DEFAULTDATA.fields_by_name['ndarray'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_DEFAULTDATA.fields_by_name['tftensor'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_DEFAULTDATA.oneofs_by_name['data_oneof'].fields.append(
  _DEFAULTDATA.fields_by_name['tensor'])
_DEFAULTDATA.fields_by_name['tensor'].containing_oneof = _DEFAULTDATA.oneofs_by_name['data_oneof']
_DEFAULTDATA.oneofs_by_name['data_oneof'].fields.append(
  _DEFAULTDATA.fields_by_name['ndarray'])
_DEFAULTDATA.fields_by_name['ndarray'].containing_oneof = _DEFAULTDATA.oneofs_by_name['data_oneof']
_DEFAULTDATA.oneofs_by_name['data_oneof'].fields.append(
  _DEFAULTDATA.fields_by_name['tftensor'])
_DEFAULTDATA.fields_by_name['tftensor'].containing_oneof = _DEFAULTDATA.oneofs_by_name['data_oneof']
_META_TAGSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_META_TAGSENTRY.containing_type = _META
_META_ROUTINGENTRY.containing_type = _META
_META_REQUESTPATHENTRY.containing_type = _META
_META.fields_by_name['tags'].message_type = _META_TAGSENTRY
_META.fields_by_name['routing'].message_type = _META_ROUTINGENTRY
_META.fields_by_name['requestPath'].message_type = _META_REQUESTPATHENTRY
_META.fields_by_name['metrics'].message_type = _METRIC
_METRIC_TAGSENTRY.containing_type = _METRIC
_METRIC.fields_by_name['type'].enum_type = _METRIC_METRICTYPE
_METRIC.fields_by_name['tags'].message_type = _METRIC_TAGSENTRY
_METRIC_METRICTYPE.containing_type = _METRIC
_SELDONMESSAGELIST.fields_by_name['seldonMessages'].message_type = _SELDONMESSAGE
_STATUS.fields_by_name['status'].enum_type = _STATUS_STATUSFLAG
_STATUS_STATUSFLAG.containing_type = _STATUS
_FEEDBACK.fields_by_name['request'].message_type = _SELDONMESSAGE
_FEEDBACK.fields_by_name['response'].message_type = _SELDONMESSAGE
_FEEDBACK.fields_by_name['truth'].message_type = _SELDONMESSAGE
_REQUESTRESPONSE.fields_by_name['request'].message_type = _SELDONMESSAGE
_REQUESTRESPONSE.fields_by_name['response'].message_type = _SELDONMESSAGE
DESCRIPTOR.message_types_by_name['SeldonMessage'] = _SELDONMESSAGE
DESCRIPTOR.message_types_by_name['DefaultData'] = _DEFAULTDATA
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['SeldonMessageList'] = _SELDONMESSAGELIST
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Feedback'] = _FEEDBACK
DESCRIPTOR.message_types_by_name['RequestResponse'] = _REQUESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SeldonMessage = _reflection.GeneratedProtocolMessageType('SeldonMessage', (_message.Message,), dict(
  DESCRIPTOR = _SELDONMESSAGE,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.SeldonMessage)
  ))
_sym_db.RegisterMessage(SeldonMessage)

DefaultData = _reflection.GeneratedProtocolMessageType('DefaultData', (_message.Message,), dict(
  DESCRIPTOR = _DEFAULTDATA,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.DefaultData)
  ))
_sym_db.RegisterMessage(DefaultData)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), dict(
  DESCRIPTOR = _TENSOR,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.Tensor)
  ))
_sym_db.RegisterMessage(Tensor)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _META_TAGSENTRY,
    __module__ = 'proto.prediction_pb2'
    # @@protoc_insertion_point(class_scope:seldon.protos.Meta.TagsEntry)
    ))
  ,

  RoutingEntry = _reflection.GeneratedProtocolMessageType('RoutingEntry', (_message.Message,), dict(
    DESCRIPTOR = _META_ROUTINGENTRY,
    __module__ = 'proto.prediction_pb2'
    # @@protoc_insertion_point(class_scope:seldon.protos.Meta.RoutingEntry)
    ))
  ,

  RequestPathEntry = _reflection.GeneratedProtocolMessageType('RequestPathEntry', (_message.Message,), dict(
    DESCRIPTOR = _META_REQUESTPATHENTRY,
    __module__ = 'proto.prediction_pb2'
    # @@protoc_insertion_point(class_scope:seldon.protos.Meta.RequestPathEntry)
    ))
  ,
  DESCRIPTOR = _META,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.Meta)
  ))
_sym_db.RegisterMessage(Meta)
_sym_db.RegisterMessage(Meta.TagsEntry)
_sym_db.RegisterMessage(Meta.RoutingEntry)
_sym_db.RegisterMessage(Meta.RequestPathEntry)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _METRIC_TAGSENTRY,
    __module__ = 'proto.prediction_pb2'
    # @@protoc_insertion_point(class_scope:seldon.protos.Metric.TagsEntry)
    ))
  ,
  DESCRIPTOR = _METRIC,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.Metric)
  ))
_sym_db.RegisterMessage(Metric)
_sym_db.RegisterMessage(Metric.TagsEntry)

SeldonMessageList = _reflection.GeneratedProtocolMessageType('SeldonMessageList', (_message.Message,), dict(
  DESCRIPTOR = _SELDONMESSAGELIST,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.SeldonMessageList)
  ))
_sym_db.RegisterMessage(SeldonMessageList)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.Status)
  ))
_sym_db.RegisterMessage(Status)

Feedback = _reflection.GeneratedProtocolMessageType('Feedback', (_message.Message,), dict(
  DESCRIPTOR = _FEEDBACK,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.Feedback)
  ))
_sym_db.RegisterMessage(Feedback)

RequestResponse = _reflection.GeneratedProtocolMessageType('RequestResponse', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTRESPONSE,
  __module__ = 'proto.prediction_pb2'
  # @@protoc_insertion_point(class_scope:seldon.protos.RequestResponse)
  ))
_sym_db.RegisterMessage(RequestResponse)


DESCRIPTOR._options = None
_TENSOR.fields_by_name['shape']._options = None
_TENSOR.fields_by_name['values']._options = None
_META_TAGSENTRY._options = None
_META_ROUTINGENTRY._options = None
_META_REQUESTPATHENTRY._options = None
_METRIC_TAGSENTRY._options = None

_GENERIC = _descriptor.ServiceDescriptor(
  name='Generic',
  full_name='seldon.protos.Generic',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1645,
  serialized_end=2038,
  methods=[
  _descriptor.MethodDescriptor(
    name='TransformInput',
    full_name='seldon.protos.Generic.TransformInput',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransformOutput',
    full_name='seldon.protos.Generic.TransformOutput',
    index=1,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Route',
    full_name='seldon.protos.Generic.Route',
    index=2,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Aggregate',
    full_name='seldon.protos.Generic.Aggregate',
    index=3,
    containing_service=None,
    input_type=_SELDONMESSAGELIST,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFeedback',
    full_name='seldon.protos.Generic.SendFeedback',
    index=4,
    containing_service=None,
    input_type=_FEEDBACK,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENERIC)

DESCRIPTOR.services_by_name['Generic'] = _GENERIC


_MODEL = _descriptor.ServiceDescriptor(
  name='Model',
  full_name='seldon.protos.Model',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=2041,
  serialized_end=2194,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='seldon.protos.Model.Predict',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFeedback',
    full_name='seldon.protos.Model.SendFeedback',
    index=1,
    containing_service=None,
    input_type=_FEEDBACK,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODEL)

DESCRIPTOR.services_by_name['Model'] = _MODEL


_ROUTER = _descriptor.ServiceDescriptor(
  name='Router',
  full_name='seldon.protos.Router',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=2197,
  serialized_end=2349,
  methods=[
  _descriptor.MethodDescriptor(
    name='Route',
    full_name='seldon.protos.Router.Route',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFeedback',
    full_name='seldon.protos.Router.SendFeedback',
    index=1,
    containing_service=None,
    input_type=_FEEDBACK,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTER)

DESCRIPTOR.services_by_name['Router'] = _ROUTER


_TRANSFORMER = _descriptor.ServiceDescriptor(
  name='Transformer',
  full_name='seldon.protos.Transformer',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=2351,
  serialized_end=2444,
  methods=[
  _descriptor.MethodDescriptor(
    name='TransformInput',
    full_name='seldon.protos.Transformer.TransformInput',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSFORMER)

DESCRIPTOR.services_by_name['Transformer'] = _TRANSFORMER


_OUTPUTTRANSFORMER = _descriptor.ServiceDescriptor(
  name='OutputTransformer',
  full_name='seldon.protos.OutputTransformer',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  serialized_start=2446,
  serialized_end=2546,
  methods=[
  _descriptor.MethodDescriptor(
    name='TransformOutput',
    full_name='seldon.protos.OutputTransformer.TransformOutput',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OUTPUTTRANSFORMER)

DESCRIPTOR.services_by_name['OutputTransformer'] = _OUTPUTTRANSFORMER


_COMBINER = _descriptor.ServiceDescriptor(
  name='Combiner',
  full_name='seldon.protos.Combiner',
  file=DESCRIPTOR,
  index=5,
  serialized_options=None,
  serialized_start=2548,
  serialized_end=2637,
  methods=[
  _descriptor.MethodDescriptor(
    name='Aggregate',
    full_name='seldon.protos.Combiner.Aggregate',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGELIST,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMBINER)

DESCRIPTOR.services_by_name['Combiner'] = _COMBINER


_SELDON = _descriptor.ServiceDescriptor(
  name='Seldon',
  full_name='seldon.protos.Seldon',
  file=DESCRIPTOR,
  index=6,
  serialized_options=None,
  serialized_start=2640,
  serialized_end=2794,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='seldon.protos.Seldon.Predict',
    index=0,
    containing_service=None,
    input_type=_SELDONMESSAGE,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFeedback',
    full_name='seldon.protos.Seldon.SendFeedback',
    index=1,
    containing_service=None,
    input_type=_FEEDBACK,
    output_type=_SELDONMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SELDON)

DESCRIPTOR.services_by_name['Seldon'] = _SELDON

# @@protoc_insertion_point(module_scope)
