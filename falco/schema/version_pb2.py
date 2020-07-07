# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='version.proto',
  package='falco.version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rversion.proto\x12\rfalco.version\"\t\n\x07request\"k\n\x08response\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\r\n\x05major\x18\x02 \x01(\r\x12\r\n\x05minor\x18\x03 \x01(\r\x12\r\n\x05patch\x18\x04 \x01(\r\x12\x12\n\nprerelease\x18\x05 \x01(\t\x12\r\n\x05\x62uild\x18\x06 \x01(\t2E\n\x07service\x12:\n\x07version\x12\x16.falco.version.request\x1a\x17.falco.version.responseb\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='request',
  full_name='falco.version.request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=32,
  serialized_end=41,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='falco.version.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='falco.version.response.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='major', full_name='falco.version.response.major', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='falco.version.response.minor', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch', full_name='falco.version.response.patch', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prerelease', full_name='falco.version.response.prerelease', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build', full_name='falco.version.response.build', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=43,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['request'] = _REQUEST
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'version_pb2'
  # @@protoc_insertion_point(class_scope:falco.version.request)
  })
_sym_db.RegisterMessage(request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'version_pb2'
  # @@protoc_insertion_point(class_scope:falco.version.response)
  })
_sym_db.RegisterMessage(response)



_SERVICE = _descriptor.ServiceDescriptor(
  name='service',
  full_name='falco.version.service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=152,
  serialized_end=221,
  methods=[
  _descriptor.MethodDescriptor(
    name='version',
    full_name='falco.version.service.version',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['service'] = _SERVICE

# @@protoc_insertion_point(module_scope)