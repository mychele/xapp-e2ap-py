# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ran_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12ran_messages.proto\"\x9f\x01\n\x13RAN_param_map_entry\x12\x1b\n\x03key\x18\x01 \x02(\x0e\x32\x0e.RAN_parameter\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x1d\n\x07ue_list\x18\x04 \x01(\x0b\x32\n.ue_list_mH\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x42\x07\n\x05value\"?\n\x16RAN_indication_request\x12%\n\rtarget_params\x18\x01 \x03(\x0e\x32\x0e.RAN_parameter\"B\n\x17RAN_indication_response\x12\'\n\tparam_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\"E\n\x13RAN_control_request\x12.\n\x10target_param_map\x18\x01 \x03(\x0b\x32\x14.RAN_param_map_entry\"\xea\x01\n\x0bRAN_message\x12#\n\x08msg_type\x18\x01 \x02(\x0e\x32\x11.RAN_message_type\x12\x39\n\x16ran_indication_request\x18\x02 \x01(\x0b\x32\x17.RAN_indication_requestH\x00\x12;\n\x17ran_indication_response\x18\x03 \x01(\x0b\x32\x18.RAN_indication_responseH\x00\x12\x33\n\x13ran_control_request\x18\x04 \x01(\x0b\x32\x14.RAN_control_requestH\x00\x42\t\n\x07payload\"\x92\x02\n\tue_info_m\x12\x0c\n\x04rnti\x18\x01 \x02(\x05\x12\x12\n\ntbs_avg_dl\x18\x02 \x01(\x02\x12\x12\n\ntbs_avg_ul\x18\x03 \x01(\x02\x12\x16\n\x0etbs_dl_toapply\x18\x04 \x01(\x02\x12\x16\n\x0etbs_ul_toapply\x18\x05 \x01(\x02\x12\x0e\n\x06is_GBR\x18\x06 \x01(\x08\x12 \n\x18\x64l_mac_buffer_occupation\x18\x07 \x01(\x02\x12\x13\n\x0b\x61vg_prbs_dl\x18\x08 \x01(\x02\x12\x13\n\x0b\x61vg_prbs_ul\x18\t \x01(\x02\x12\x0b\n\x03mcs\x18\n \x01(\x05\x12\x1a\n\x12\x61vg_tbs_per_prb_dl\x18\x0b \x01(\x02\x12\x1a\n\x12\x61vg_tbs_per_prb_ul\x18\x0c \x01(\x02\"?\n\tue_list_m\x12\x15\n\rconnected_ues\x18\x01 \x02(\x05\x12\x1b\n\x07ue_info\x18\x02 \x03(\x0b\x32\n.ue_info_m\"2\n\x0fsched_control_m\x12\x1f\n\x17max_cell_allocable_prbs\x18\x01 \x01(\x05*v\n\x10RAN_message_type\x12\x10\n\x0cSUBSCRIPTION\x10\x01\x12\x16\n\x12INDICATION_REQUEST\x10\x02\x12\x17\n\x13INDICATION_RESPONSE\x10\x03\x12\x0b\n\x07\x43ONTROL\x10\x04\x12\x12\n\x0eSOMETHING_ELSE\x10\x05*z\n\rRAN_parameter\x12\n\n\x06GNB_ID\x10\x01\x12\r\n\tSOMETHING\x10\x02\x12\x0b\n\x07UE_LIST\x10\x03\x12\x0f\n\x0bSCHED_INFO_\x10\x04\x12\x11\n\rSCHED_CONTROL\x10\x05\x12\x0b\n\x07MAX_PRB\x10\x06\x12\x10\n\x0cUSE_TRUE_GBR\x10\x07')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ran_messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RAN_MESSAGE_TYPE._serialized_start=1019
  _RAN_MESSAGE_TYPE._serialized_end=1137
  _RAN_PARAMETER._serialized_start=1139
  _RAN_PARAMETER._serialized_end=1261
  _RAN_PARAM_MAP_ENTRY._serialized_start=23
  _RAN_PARAM_MAP_ENTRY._serialized_end=182
  _RAN_INDICATION_REQUEST._serialized_start=184
  _RAN_INDICATION_REQUEST._serialized_end=247
  _RAN_INDICATION_RESPONSE._serialized_start=249
  _RAN_INDICATION_RESPONSE._serialized_end=315
  _RAN_CONTROL_REQUEST._serialized_start=317
  _RAN_CONTROL_REQUEST._serialized_end=386
  _RAN_MESSAGE._serialized_start=389
  _RAN_MESSAGE._serialized_end=623
  _UE_INFO_M._serialized_start=626
  _UE_INFO_M._serialized_end=900
  _UE_LIST_M._serialized_start=902
  _UE_LIST_M._serialized_end=965
  _SCHED_CONTROL_M._serialized_start=967
  _SCHED_CONTROL_M._serialized_end=1017
# @@protoc_insertion_point(module_scope)
