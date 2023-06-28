# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_toto_attestation/predicates/vsa/v0/vsa.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/in_toto_attestation/predicates/vsa/v0/vsa.proto\x12%in_toto_attestation.predicates.vsa.v0\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x08\n\x13VerificationSummary\x12U\n\x08verifier\x18\x01 \x01(\x0b\x32\x43.in_toto_attestation.predicates.vsa.v0.VerificationSummary.Verifier\x12?\n\x0ctimeVerified\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rtime_verified\x12!\n\x0bresourceUri\x18\x03 \x01(\tR\x0cresource_uri\x12Q\n\x06policy\x18\x04 \x01(\x0b\x32\x41.in_toto_attestation.predicates.vsa.v0.VerificationSummary.Policy\x12z\n\x11inputAttestations\x18\x05 \x03(\x0b\x32K.in_toto_attestation.predicates.vsa.v0.VerificationSummary.InputAttestationR\x12input_attestations\x12/\n\x12verificationResult\x18\x06 \x01(\tR\x13verification_result\x12!\n\x0bpolicyLevel\x18\x07 \x01(\tR\x0cpolicy_level\x12}\n\x10\x64\x65pendencyLevels\x18\x08 \x03(\x0b\x32P.in_toto_attestation.predicates.vsa.v0.VerificationSummary.DependencyLevelsEntryR\x11\x64\x65pendency_levels\x1a\x16\n\x08Verifier\x12\n\n\x02id\x18\x01 \x01(\t\x1a\xa3\x01\n\x06Policy\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12]\n\x06\x64igest\x18\x02 \x03(\x0b\x32M.in_toto_attestation.predicates.vsa.v0.VerificationSummary.Policy.DigestEntry\x1a-\n\x0b\x44igestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xb7\x01\n\x10InputAttestation\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12g\n\x06\x64igest\x18\x02 \x03(\x0b\x32W.in_toto_attestation.predicates.vsa.v0.VerificationSummary.InputAttestation.DigestEntry\x1a-\n\x0b\x44igestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15\x44\x65pendencyLevelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x42\x65\n.io.github.intoto.attestation.predicates.vsa.v0Z3github.com/in-toto/attestation/go/predicates/vsa/v0b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'in_toto_attestation.predicates.vsa.v0.vsa_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n.io.github.intoto.attestation.predicates.vsa.v0Z3github.com/in-toto/attestation/go/predicates/vsa/v0'
  _VERIFICATIONSUMMARY_POLICY_DIGESTENTRY._options = None
  _VERIFICATIONSUMMARY_POLICY_DIGESTENTRY._serialized_options = b'8\001'
  _VERIFICATIONSUMMARY_INPUTATTESTATION_DIGESTENTRY._options = None
  _VERIFICATIONSUMMARY_INPUTATTESTATION_DIGESTENTRY._serialized_options = b'8\001'
  _VERIFICATIONSUMMARY_DEPENDENCYLEVELSENTRY._options = None
  _VERIFICATIONSUMMARY_DEPENDENCYLEVELSENTRY._serialized_options = b'8\001'
  _VERIFICATIONSUMMARY._serialized_start=124
  _VERIFICATIONSUMMARY._serialized_end=1183
  _VERIFICATIONSUMMARY_VERIFIER._serialized_start=752
  _VERIFICATIONSUMMARY_VERIFIER._serialized_end=774
  _VERIFICATIONSUMMARY_POLICY._serialized_start=777
  _VERIFICATIONSUMMARY_POLICY._serialized_end=940
  _VERIFICATIONSUMMARY_POLICY_DIGESTENTRY._serialized_start=895
  _VERIFICATIONSUMMARY_POLICY_DIGESTENTRY._serialized_end=940
  _VERIFICATIONSUMMARY_INPUTATTESTATION._serialized_start=943
  _VERIFICATIONSUMMARY_INPUTATTESTATION._serialized_end=1126
  _VERIFICATIONSUMMARY_INPUTATTESTATION_DIGESTENTRY._serialized_start=895
  _VERIFICATIONSUMMARY_INPUTATTESTATION_DIGESTENTRY._serialized_end=940
  _VERIFICATIONSUMMARY_DEPENDENCYLEVELSENTRY._serialized_start=1128
  _VERIFICATIONSUMMARY_DEPENDENCYLEVELSENTRY._serialized_end=1183
# @@protoc_insertion_point(module_scope)
