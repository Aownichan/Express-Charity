# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12proto/server.proto\x12\x0cverification\"\x1f\n\rImageNamesReq\x12\x0e\n\x06images\x18\x01 \x03(\t\"\x90\x01\n\x0ePredictionsRes\x12\x36\n\x05preds\x18\x01 \x03(\x0b\x32\'.verification.PredictionsRes.PredsEntry\x1a\x46\n\nPredsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.verification.Prediction:\x02\x38\x01\"/\n\nPrediction\x12\x11\n\tincidents\x18\x01 \x03(\t\x12\x0e\n\x06places\x18\x02 \x03(\t2]\n\x10\x42\x65n_Verification\x12I\n\x0cVerifyImages\x12\x1b.verification.ImageNamesReq\x1a\x1c.verification.PredictionsResb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREDICTIONSRES_PREDSENTRY._options = None
  _PREDICTIONSRES_PREDSENTRY._serialized_options = b'8\001'
  _IMAGENAMESREQ._serialized_start=36
  _IMAGENAMESREQ._serialized_end=67
  _PREDICTIONSRES._serialized_start=70
  _PREDICTIONSRES._serialized_end=214
  _PREDICTIONSRES_PREDSENTRY._serialized_start=144
  _PREDICTIONSRES_PREDSENTRY._serialized_end=214
  _PREDICTION._serialized_start=216
  _PREDICTION._serialized_end=263
  _BEN_VERIFICATION._serialized_start=265
  _BEN_VERIFICATION._serialized_end=358
# @@protoc_insertion_point(module_scope)
