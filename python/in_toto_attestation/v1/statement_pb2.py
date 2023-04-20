# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_toto_attestation/v1/statement.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='in_toto_attestation/v1/statement.proto',
  package='in_toto_attestation.v1',
  syntax='proto3',
  serialized_options=b'Z$github.com/in-toto/attestation/go/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&in_toto_attestation/v1/statement.proto\x12\x16in_toto_attestation.v1\x1a\x1cgoogle/protobuf/struct.proto\"\xaf\x02\n\tStatement\x12\x13\n\x04type\x18\x01 \x01(\tR\x05_type\x12:\n\x07subject\x18\x02 \x03(\x0b\x32).in_toto_attestation.v1.Statement.Subject\x12\x15\n\rpredicateType\x18\x03 \x01(\t\x12*\n\tpredicate\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x8d\x01\n\x07Subject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x06\x64igest\x18\x02 \x03(\x0b\x32\x35.in_toto_attestation.v1.Statement.Subject.DigestEntry\x1a-\n\x0b\x44igestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42&Z$github.com/in-toto/attestation/go/v1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_STATEMENT_SUBJECT_DIGESTENTRY = _descriptor.Descriptor(
  name='DigestEntry',
  full_name='in_toto_attestation.v1.Statement.Subject.DigestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='in_toto_attestation.v1.Statement.Subject.DigestEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='in_toto_attestation.v1.Statement.Subject.DigestEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=400,
)

_STATEMENT_SUBJECT = _descriptor.Descriptor(
  name='Subject',
  full_name='in_toto_attestation.v1.Statement.Subject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='in_toto_attestation.v1.Statement.Subject.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='in_toto_attestation.v1.Statement.Subject.digest', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STATEMENT_SUBJECT_DIGESTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=400,
)

_STATEMENT = _descriptor.Descriptor(
  name='Statement',
  full_name='in_toto_attestation.v1.Statement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='in_toto_attestation.v1.Statement.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='_type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='in_toto_attestation.v1.Statement.subject', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='predicateType', full_name='in_toto_attestation.v1.Statement.predicateType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='predicate', full_name='in_toto_attestation.v1.Statement.predicate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STATEMENT_SUBJECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=400,
)

_STATEMENT_SUBJECT_DIGESTENTRY.containing_type = _STATEMENT_SUBJECT
_STATEMENT_SUBJECT.fields_by_name['digest'].message_type = _STATEMENT_SUBJECT_DIGESTENTRY
_STATEMENT_SUBJECT.containing_type = _STATEMENT
_STATEMENT.fields_by_name['subject'].message_type = _STATEMENT_SUBJECT
_STATEMENT.fields_by_name['predicate'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['Statement'] = _STATEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Statement = _reflection.GeneratedProtocolMessageType('Statement', (_message.Message,), {

  'Subject' : _reflection.GeneratedProtocolMessageType('Subject', (_message.Message,), {

    'DigestEntry' : _reflection.GeneratedProtocolMessageType('DigestEntry', (_message.Message,), {
      'DESCRIPTOR' : _STATEMENT_SUBJECT_DIGESTENTRY,
      '__module__' : 'in_toto_attestation.v1.statement_pb2'
      # @@protoc_insertion_point(class_scope:in_toto_attestation.v1.Statement.Subject.DigestEntry)
      })
    ,
    'DESCRIPTOR' : _STATEMENT_SUBJECT,
    '__module__' : 'in_toto_attestation.v1.statement_pb2'
    # @@protoc_insertion_point(class_scope:in_toto_attestation.v1.Statement.Subject)
    })
  ,
  'DESCRIPTOR' : _STATEMENT,
  '__module__' : 'in_toto_attestation.v1.statement_pb2'
  # @@protoc_insertion_point(class_scope:in_toto_attestation.v1.Statement)
  })
_sym_db.RegisterMessage(Statement)
_sym_db.RegisterMessage(Statement.Subject)
_sym_db.RegisterMessage(Statement.Subject.DigestEntry)


DESCRIPTOR._options = None
_STATEMENT_SUBJECT_DIGESTENTRY._options = None
# @@protoc_insertion_point(module_scope)