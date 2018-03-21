import babeltrace
import babeltrace.reader as btr
import babeltrace.writer as btw

# Create field declarations
# Field declarations
uint64_fd = btw.IntegerFieldDeclaration(64)
uint64_fd.signed = False

int64_fd = btw.IntegerFieldDeclaration(64)
int64_fd.signed = True

uint32_fd = btw.IntegerFieldDeclaration(32)
uint32_fd.signed = False

int32_fd = btw.IntegerFieldDeclaration(32)
int32_fd.signed = True

float_fd = btw.FloatingPointFieldDeclaration()

huint64_fd = btw.IntegerFieldDeclaration(64)
huint64_fd.base = babeltrace.writer.IntegerBase.HEX
huint64_fd.signed = False

string_fd = btw.StringFieldDeclaration()

dim_array_fd = btw.ArrayFieldDeclaration(uint32_fd, 3)
# Create event classes
event_classes = {}

# Paul
event_classes['hsa_runtime:kernel_start_nm'] = btw.EventClass('hsa_runtime:kernel_start_nm')
event_classes['hsa_runtime:kernel_start_nm'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:kernel_start_nm'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:kernel_start_nm'].add_field(string_fd, 'name')
event_classes['hsa_runtime:kernel_start_nm'].add_field(uint64_fd, 'agent_handle')
event_classes['hsa_runtime:kernel_start_nm'].add_field(uint64_fd, 'queue_id')
event_classes['hsa_runtime:kernel_start_nm'].add_field(uint64_fd, 'timestamp')

event_classes['hsa_runtime:kernel_end_nm'] = btw.EventClass('hsa_runtime:kernel_end_nm')
event_classes['hsa_runtime:kernel_end_nm'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:kernel_end_nm'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:kernel_end_nm'].add_field(string_fd, 'name')
event_classes['hsa_runtime:kernel_end_nm'].add_field(uint64_fd, 'agent_handle')
event_classes['hsa_runtime:kernel_end_nm'].add_field(uint64_fd, 'queue_id')
event_classes['hsa_runtime:kernel_end_nm'].add_field(uint64_fd, 'timestamp')

event_classes['hsa_runtime:runtime_initialized'] = btw.EventClass('hsa_runtime:runtime_initialized')
event_classes['hsa_runtime:runtime_initialized'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:runtime_shut_down'] = btw.EventClass('hsa_runtime:runtime_shut_down')
event_classes['hsa_runtime:runtime_shut_down'].add_field(string_fd, 'cat')

event_classes['hsa_runtime:queue_created'] = btw.EventClass('hsa_runtime:queue_created')
event_classes['hsa_runtime:queue_created'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:queue_created'].add_field(uint64_fd, 'agent_handle')
event_classes['hsa_runtime:queue_created'].add_field(uint64_fd, 'queue_id')
event_classes['hsa_runtime:queue_destroyed'] = btw.EventClass('hsa_runtime:queue_destroyed')
event_classes['hsa_runtime:queue_destroyed'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:queue_destroyed'].add_field(uint64_fd, 'queue_id')

event_classes['hsa_runtime:aql_packet_submitted'] = btw.EventClass('hsa_runtime:aql_packet_submitted')
event_classes['hsa_runtime:aql_packet_submitted'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:aql_packet_submitted'].add_field(uint64_fd, 'packet_id')
event_classes['hsa_runtime:aql_packet_submitted'].add_field(string_fd, 'packet_type')
event_classes['hsa_runtime:aql_packet_submitted'].add_field(uint64_fd, 'agent_handle')
event_classes['hsa_runtime:aql_packet_submitted'].add_field(uint64_fd, 'queue_id')

event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'] = btw.EventClass('hsa_runtime:aql_kernel_dispatch_packet_submitted')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'packet_id')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'agent_handle')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'queue_id')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:aql_kernel_dispatch_packet_submitted'].add_field(string_fd, 'kernel_name')


event_classes['hsa_runtime:perf_counter_uint32'] = btw.EventClass('hsa_runtime:perf_counter_uint32')
event_classes['hsa_runtime:perf_counter_uint32'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:perf_counter_uint32'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:perf_counter_uint32'].add_field(uint32_fd, 'counter_index')
event_classes['hsa_runtime:perf_counter_uint32'].add_field(string_fd, 'counter_name')
event_classes['hsa_runtime:perf_counter_uint32'].add_field(uint32_fd, 'value')

event_classes['hsa_runtime:perf_counter_uint64'] = btw.EventClass('hsa_runtime:perf_counter_uint64')
event_classes['hsa_runtime:perf_counter_uint64'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:perf_counter_uint64'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:perf_counter_uint64'].add_field(uint32_fd, 'counter_index')
event_classes['hsa_runtime:perf_counter_uint64'].add_field(string_fd, 'counter_name')
event_classes['hsa_runtime:perf_counter_uint64'].add_field(uint64_fd, 'value')


event_classes['hsa_runtime:perf_counter_float32'] = btw.EventClass('hsa_runtime:perf_counter_float32')
event_classes['hsa_runtime:perf_counter_float32'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:perf_counter_float32'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:perf_counter_float32'].add_field(uint32_fd, 'counter_index')
event_classes['hsa_runtime:perf_counter_float32'].add_field(string_fd, 'counter_name')
event_classes['hsa_runtime:perf_counter_float32'].add_field(float_fd, 'value')

event_classes['hsa_runtime:perf_counter_float64'] = btw.EventClass('hsa_runtime:perf_counter_float64')
event_classes['hsa_runtime:perf_counter_float64'].add_field(string_fd, 'cat')
event_classes['hsa_runtime:perf_counter_float64'].add_field(uint64_fd, 'kernel_object')
event_classes['hsa_runtime:perf_counter_float64'].add_field(uint32_fd, 'counter_index')
event_classes['hsa_runtime:perf_counter_float64'].add_field(string_fd, 'counter_name')
event_classes['hsa_runtime:perf_counter_float64'].add_field(float_fd, 'value')




# hsaTracer
event_classes['hsaTracer:function_entry'] = btw.EventClass('hsaTracer:function_entry')
event_classes['hsaTracer:function_entry'].add_field(string_fd, 'cat')
event_classes['hsaTracer:function_entry'].add_field(string_fd, 'name')
event_classes['hsaTracer:function_exit'] = btw.EventClass('hsaTracer:function_exit')
event_classes['hsaTracer:function_exit'].add_field(string_fd, 'cat')
event_classes['hsaTracer:function_exit'].add_field(string_fd, 'name')
event_classes['hsaTracer:pool_memory_allocate'] = btw.EventClass('hsaTracer:pool_memory_allocate')
event_classes['hsaTracer:pool_memory_allocate'].add_field(uint64_fd, 'handle')
event_classes['hsaTracer:pool_memory_allocate'].add_field(uint64_fd, 'ptr')
event_classes['hsaTracer:pool_memory_allocate'].add_field(uint64_fd, 'size')
event_classes['hsaTracer:pool_memory_free'] = btw.EventClass('hsaTracer:pool_memory_free')
event_classes['hsaTracer:pool_memory_free'].add_field(uint64_fd, 'handle')
event_classes['hsaTracer:pool_memory_free'].add_field(uint64_fd, 'ptr')
event_classes['hsaTracer:pool_memory_free'].add_field(int64_fd, 'size')

# hipTracer
event_classes['hipTracer:function_entry'] = btw.EventClass('hipTracer:function_entry')
event_classes['hipTracer:function_entry'].add_field(string_fd, 'cat')
event_classes['hipTracer:function_entry'].add_field(string_fd, 'name')
event_classes['hipTracer:function_exit'] = btw.EventClass('hipTracer:function_exit')
event_classes['hipTracer:function_exit'].add_field(string_fd, 'cat')
event_classes['hipTracer:function_exit'].add_field(string_fd, 'name')
event_classes['hipTracer:wait_begin'] = btw.EventClass('hipTracer:wait_begin')
event_classes['hipTracer:wait_begin'].add_field(string_fd, 'cat')
event_classes['hipTracer:wait_begin'].add_field(string_fd, 'name')
event_classes['hipTracer:wait_end'] = btw.EventClass('hipTracer:wait_end')
event_classes['hipTracer:wait_end'].add_field(string_fd, 'cat')
event_classes['hipTracer:wait_end'].add_field(string_fd, 'name')

# grpcTracer
event_classes['grpcTracer:receive_request'] = btw.EventClass('grpcTracer:receive_request')
event_classes['grpcTracer:receive_request'].add_field(string_fd, 'name')
event_classes['grpcTracer:send_request'] = btw.EventClass('grpcTracer:send_request')
event_classes['grpcTracer:send_request'].add_field(string_fd, 'name')

event_classes['grpcTracer:receive_RecvTensor_request'] = btw.EventClass('grpcTracer:receive_RecvTensor_request')
event_classes['grpcTracer:receive_RecvTensor_request'].add_field(string_fd, 'cat')
event_classes['grpcTracer:receive_RecvTensor_request'].add_field(string_fd, 'name')
event_classes['grpcTracer:receive_RecvTensor_request'].add_field(string_fd, 'rendezvous_key')
event_classes['grpcTracer:receive_RecvTensor_request'].add_field(uint64_fd, 'step_id')
event_classes['grpcTracer:receive_RecvTensor_request'].add_field(uint32_fd, 'bus_id')
event_classes['grpcTracer:send_RecvTensor_request'] = btw.EventClass('grpcTracer:send_RecvTensor_request')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'cat')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'name')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'rendezvous_key')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'tensor')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'src_device')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'dst_device')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'request')
event_classes['grpcTracer:send_RecvTensor_request'].add_field(string_fd, 'response')

event_classes['grpcTracer:set_proto_from_gpu_start'] = btw.EventClass('grpcTracer:set_proto_from_gpu_start')
event_classes['grpcTracer:set_proto_from_gpu_start'].add_field(string_fd, 'cat')
event_classes['grpcTracer:set_proto_from_gpu_start'].add_field(string_fd, 'name')
event_classes['grpcTracer:set_proto_from_gpu_start'].add_field(string_fd, 'rendezvous_key')
event_classes['grpcTracer:set_proto_from_gpu_end'] = btw.EventClass('grpcTracer:set_proto_from_gpu_end')
event_classes['grpcTracer:set_proto_from_gpu_end'].add_field(string_fd, 'cat')
event_classes['grpcTracer:set_proto_from_gpu_end'].add_field(string_fd, 'name')
event_classes['grpcTracer:set_proto_from_gpu_end'].add_field(string_fd, 'rendezvous_key')

event_classes['grpcTracer:prepare_response_tensor_start'] = btw.EventClass('grpcTracer:prepare_response_tensor_start')
event_classes['grpcTracer:prepare_response_tensor_start'].add_field(string_fd, 'cat')
event_classes['grpcTracer:prepare_response_tensor_start'].add_field(string_fd, 'name')
event_classes['grpcTracer:prepare_response_tensor_start'].add_field(string_fd, 'rendezvous_key')
event_classes['grpcTracer:prepare_response_tensor_end'] = btw.EventClass('grpcTracer:prepare_response_tensor_end')
event_classes['grpcTracer:prepare_response_tensor_end'].add_field(string_fd, 'cat')
event_classes['grpcTracer:prepare_response_tensor_end'].add_field(string_fd, 'name')
event_classes['grpcTracer:prepare_response_tensor_end'].add_field(string_fd, 'rendezvous_key')

event_classes['grpcTracer:send_request_tensor_start'] = btw.EventClass('grpcTracer:send_request_tensor_start')
event_classes['grpcTracer:send_request_tensor_start'].add_field(string_fd, 'cat')
event_classes['grpcTracer:send_request_tensor_start'].add_field(string_fd, 'name')
event_classes['grpcTracer:send_request_tensor_start'].add_field(string_fd, 'rendezvous_key')
event_classes['grpcTracer:send_request_tensor_end'] = btw.EventClass('grpcTracer:send_request_tensor_end')
event_classes['grpcTracer:send_request_tensor_end'].add_field(string_fd, 'cat')
event_classes['grpcTracer:send_request_tensor_end'].add_field(string_fd, 'name')
event_classes['grpcTracer:send_request_tensor_end'].add_field(string_fd, 'rendezvous_key')


# STREAM TRACERS
event_classes['streamTracer:stream_then_memcpy_host_to_device_start'] = btw.EventClass('streamTracer:stream_then_memcpy_host_to_device_start')
event_classes['streamTracer:stream_then_memcpy_host_to_device_start'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_host_to_device_start'].add_field(string_fd, 'name')
event_classes['streamTracer:stream_then_memcpy_host_to_device_end'] = btw.EventClass('streamTracer:stream_then_memcpy_host_to_device_end')
event_classes['streamTracer:stream_then_memcpy_host_to_device_end'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_host_to_device_end'].add_field(string_fd, 'name')

event_classes['streamTracer:stream_then_memcpy_device_to_host_start'] = btw.EventClass('streamTracer:stream_then_memcpy_device_to_host_start')
event_classes['streamTracer:stream_then_memcpy_device_to_host_start'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_device_to_host_start'].add_field(string_fd, 'name')
event_classes['streamTracer:stream_then_memcpy_device_to_host_end'] = btw.EventClass('streamTracer:stream_then_memcpy_device_to_host_end')
event_classes['streamTracer:stream_then_memcpy_device_to_host_end'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_device_to_host_end'].add_field(string_fd, 'name')

event_classes['streamTracer:stream_then_memcpy_device_to_device_start'] = btw.EventClass('streamTracer:stream_then_memcpy_device_to_device_start')
event_classes['streamTracer:stream_then_memcpy_device_to_device_start'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_device_to_device_start'].add_field(string_fd, 'name')
event_classes['streamTracer:stream_then_memcpy_device_to_device_end'] = btw.EventClass('streamTracer:stream_then_memcpy_device_to_device_end')
event_classes['streamTracer:stream_then_memcpy_device_to_device_end'].add_field(string_fd, 'cat')
event_classes['streamTracer:stream_then_memcpy_device_to_device_end'].add_field(string_fd, 'name')

# hccTracer
event_classes['hccTracer:kernel_begin'] = btw.EventClass('hccTracer:kernel_begin')
event_classes['hccTracer:kernel_begin'].add_field(string_fd, 'cat')
event_classes['hccTracer:kernel_begin'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:kernel_begin'].add_field(string_fd, 'name')
event_classes['hccTracer:kernel_begin'].add_field(string_fd, 'long_name')
event_classes['hccTracer:kernel_begin'].add_field(string_fd, 'tf_name')
event_classes['hccTracer:kernel_begin'].add_field(dim_array_fd, 'workgroup_size')
event_classes['hccTracer:kernel_begin'].add_field(dim_array_fd, 'grid_size')
event_classes['hccTracer:kernel_begin'].add_field(uint32_fd, 'static_group_segment_size')
event_classes['hccTracer:kernel_begin'].add_field(uint32_fd, 'private_segment_size')
event_classes['hccTracer:kernel_begin'].add_field(uint32_fd, 'workitem_vgpr_count')

event_classes['hccTracer:kernel_end'] = btw.EventClass('hccTracer:kernel_end')
event_classes['hccTracer:kernel_end'].add_field(string_fd, 'cat')
event_classes['hccTracer:kernel_end'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:kernel_end'].add_field(string_fd, 'name')
event_classes['hccTracer:kernel_end'].add_field(string_fd, 'long_name')
event_classes['hccTracer:kernel_end'].add_field(string_fd, 'tf_name')
event_classes['hccTracer:kernel_end'].add_field(dim_array_fd, 'workgroup_size')
event_classes['hccTracer:kernel_end'].add_field(dim_array_fd, 'grid_size')
event_classes['hccTracer:kernel_end'].add_field(uint32_fd, 'static_group_segment_size')
event_classes['hccTracer:kernel_end'].add_field(uint32_fd, 'private_segment_size')
event_classes['hccTracer:kernel_end'].add_field(uint32_fd, 'workitem_vgpr_count')

event_classes['hccTracer:unpinned_memory_engine_copy_entry'] = btw.EventClass('hccTracer:unpinned_memory_engine_copy_entry')
event_classes['hccTracer:unpinned_memory_engine_copy_entry'].add_field(string_fd, 'cat')
event_classes['hccTracer:unpinned_memory_engine_copy_entry'].add_field(string_fd, 'name')
event_classes['hccTracer:unpinned_memory_engine_copy_entry'].add_field(int64_fd, 'size_bytes')
event_classes['hccTracer:unpinned_memory_engine_copy_exit'] = btw.EventClass('hccTracer:unpinned_memory_engine_copy_exit')
event_classes['hccTracer:unpinned_memory_engine_copy_exit'].add_field(string_fd, 'cat')
event_classes['hccTracer:unpinned_memory_engine_copy_exit'].add_field(string_fd, 'name')
event_classes['hccTracer:unpinned_memory_engine_copy_exit'].add_field(int64_fd, 'size_bytes')

event_classes['hccTracer:async_memcpy_begin'] = btw.EventClass('hccTracer:async_memcpy_begin')
event_classes['hccTracer:async_memcpy_begin'].add_field(string_fd, 'cat')
event_classes['hccTracer:async_memcpy_begin'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:async_memcpy_begin'].add_field(string_fd, 'name')
event_classes['hccTracer:async_memcpy_begin'].add_field(int64_fd, 'size_bytes')
event_classes['hccTracer:async_memcpy_begin'].add_field(float_fd, 'size_megabytes')
event_classes['hccTracer:async_memcpy_begin'].add_field(float_fd, 'throughput')
event_classes['hccTracer:async_memcpy_begin'].add_field(uint32_fd, 'isAsync')
event_classes['hccTracer:async_memcpy_begin'].add_field(uint32_fd, 'isSingleStepCopy')
event_classes['hccTracer:async_memcpy_begin'].add_field(uint32_fd, 'isPeerToPeer')
event_classes['hccTracer:async_memcpy_begin'].add_field(uint32_fd, 'isActiveWait')

event_classes['hccTracer:async_memcpy_end'] = btw.EventClass('hccTracer:async_memcpy_end')
event_classes['hccTracer:async_memcpy_end'].add_field(string_fd, 'cat')
event_classes['hccTracer:async_memcpy_end'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:async_memcpy_end'].add_field(string_fd, 'name')
event_classes['hccTracer:async_memcpy_end'].add_field(int64_fd, 'size_bytes')
event_classes['hccTracer:async_memcpy_end'].add_field(float_fd, 'size_megabytes')
event_classes['hccTracer:async_memcpy_end'].add_field(float_fd, 'throughput')
event_classes['hccTracer:async_memcpy_end'].add_field(uint32_fd, 'isAsync')
event_classes['hccTracer:async_memcpy_end'].add_field(uint32_fd, 'isSingleStepCopy')
event_classes['hccTracer:async_memcpy_end'].add_field(uint32_fd, 'isPeerToPeer')
event_classes['hccTracer:async_memcpy_end'].add_field(uint32_fd, 'isActiveWait')

event_classes['hccTracer:async_memcpyslo_begin'] = btw.EventClass('hccTracer:async_memcpy_begin')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(string_fd, 'cat')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(string_fd, 'name')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(int64_fd, 'size_bytes')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(float_fd, 'size_megabytes')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(float_fd, 'throughput')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(uint32_fd, 'isAsync')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(uint32_fd, 'isSingleStepCopy')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(uint32_fd, 'isPeerToPeer')
event_classes['hccTracer:async_memcpyslo_begin'].add_field(uint32_fd, 'isActiveWait')

event_classes['hccTracer:async_memcpyslo_end'] = btw.EventClass('hccTracer:async_memcpy_end')
event_classes['hccTracer:async_memcpyslo_end'].add_field(string_fd, 'cat')
event_classes['hccTracer:async_memcpyslo_end'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:async_memcpyslo_end'].add_field(string_fd, 'name')
event_classes['hccTracer:async_memcpyslo_end'].add_field(int64_fd, 'size_bytes')
event_classes['hccTracer:async_memcpyslo_end'].add_field(float_fd, 'size_megabytes')
event_classes['hccTracer:async_memcpyslo_end'].add_field(float_fd, 'throughput')
event_classes['hccTracer:async_memcpyslo_end'].add_field(uint32_fd, 'isAsync')
event_classes['hccTracer:async_memcpyslo_end'].add_field(uint32_fd, 'isSingleStepCopy')
event_classes['hccTracer:async_memcpyslo_end'].add_field(uint32_fd, 'isPeerToPeer')
event_classes['hccTracer:async_memcpyslo_end'].add_field(uint32_fd, 'isActiveWait')


event_classes['hccTracer:barrier_begin'] = btw.EventClass('hccTracer:barrier_begin')
event_classes['hccTracer:barrier_begin'].add_field(string_fd, 'cat')
event_classes['hccTracer:barrier_begin'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:barrier_begin'].add_field(string_fd, 'name')
event_classes['hccTracer:barrier_begin'].add_field(uint32_fd, 'dep_count')
event_classes['hccTracer:barrier_begin'].add_field(uint32_fd, 'acquire')
event_classes['hccTracer:barrier_begin'].add_field(uint32_fd, 'release')

event_classes['hccTracer:barrier_end'] = btw.EventClass('hccTracer:barrier_end')
event_classes['hccTracer:barrier_end'].add_field(string_fd, 'cat')
event_classes['hccTracer:barrier_end'].add_field(string_fd, 'name')
event_classes['hccTracer:barrier_end'].add_field(uint64_fd, 'timestamp')
event_classes['hccTracer:barrier_end'].add_field(uint32_fd, 'dep_count')
event_classes['hccTracer:barrier_end'].add_field(uint32_fd, 'acquire')
event_classes['hccTracer:barrier_end'].add_field(uint32_fd, 'release')


event_classes['hccTracer:queue_stats'] = btw.EventClass('hccTracer:queue_stats')
event_classes['hccTracer:queue_stats'].add_field(string_fd, 'queue_id')
event_classes['hccTracer:queue_stats'].add_field(uint64_fd, 'size')

# event_classes['hccTracer:aql_packet_submitted'] = btw.EventClass('hccTracer:aql_packet_submitted')
# event_classes['hccTracer:aql_packet_submitted'].add_field(uint64_fd, 'packet_id')
# event_classes['hccTracer:aql_packet_submitted'].add_field(string_fd, 'packet_type')
# event_classes['hccTracer:aql_packet_submitted'].add_field(uint64_fd, 'queue_id')
# event_classes['hccTracer:aql_packet_submitted'].add_field(uint64_fd, 'agent_handle')
# event_classes['hccTracer:aql_packet_submitted'].add_field(uint64_fd, 'queue_id')
#
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'] = btw.EventClass('hccTracer:aql_packet_submitted')
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'packet_id')
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'agent_handle')
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'queue_id')
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'].add_field(uint64_fd, 'kernel_object')
# event_classes['hccTracer:aql_kernel_dispatch_packet_submitted'].add_field(string_fd, 'kernel_name')



# tensorflowTracer

# Tracepoints : entry / exit
event_classes['tensorflowTracer:process_entry'] = btw.EventClass('tensorflowTracer:process_entry')
event_classes['tensorflowTracer:process_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:process_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:process_entry'].add_field(uint64_fd, 'schedule')
event_classes['tensorflowTracer:process_exit'] = btw.EventClass('tensorflowTracer:process_exit')
event_classes['tensorflowTracer:process_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:process_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:process_exit'].add_field(uint64_fd, 'schedule')

event_classes['tensorflowTracer:inline_ready_entry'] = btw.EventClass('tensorflowTracer:inline_ready_entry')
event_classes['tensorflowTracer:inline_ready_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:inline_ready_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:inline_ready_exit'] = btw.EventClass('tensorflowTracer:inline_ready_exit')
event_classes['tensorflowTracer:inline_ready_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:inline_ready_exit'].add_field(string_fd, 'name')

event_classes['tensorflowTracer:push_succ_entry'] = btw.EventClass('tensorflowTracer:push_succ_entry')
event_classes['tensorflowTracer:push_succ_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:push_succ_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:push_succ_exit'] = btw.EventClass('tensorflowTracer:push_succ_exit')
event_classes['tensorflowTracer:push_succ_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:push_succ_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:push_succ_exit'].add_field(uint32_fd, 'is_ready')

event_classes['tensorflowTracer:allocate_chunk_entry'] = btw.EventClass('tensorflowTracer:allocate_chunk_entry')
event_classes['tensorflowTracer:allocate_chunk_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:allocate_chunk_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:allocate_chunk_exit'] = btw.EventClass('tensorflowTracer:allocate_chunk_exit')
event_classes['tensorflowTracer:allocate_chunk_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:allocate_chunk_exit'].add_field(string_fd, 'name')

event_classes['tensorflowTracer:allocate_raw_internal_entry'] = btw.EventClass('tensorflowTracer:allocate_raw_internal_entry')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(string_fd, 'alloc_name')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(string_fd, 'ptr')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(uint32_fd, 'num_bytes')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(uint32_fd, 'rounded_bytes')
event_classes['tensorflowTracer:allocate_raw_internal_entry'].add_field(uint32_fd, 'bin_num')
event_classes['tensorflowTracer:allocate_raw_internal_exit'] = btw.EventClass('tensorflowTracer:allocate_raw_internal_exit')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(string_fd, 'alloc_name')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(string_fd, 'ptr')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(uint32_fd, 'num_bytes')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(uint32_fd, 'rounded_bytes')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(uint32_fd, 'bin_num')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(uint32_fd, 'need_extend')
event_classes['tensorflowTracer:allocate_raw_internal_exit'].add_field(uint32_fd, 'success')

event_classes['tensorflowTracer:deallocate_raw_internal_entry'] = btw.EventClass('tensorflowTracer:deallocate_raw_internal_entry')
event_classes['tensorflowTracer:deallocate_raw_internal_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:deallocate_raw_internal_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:deallocate_raw_internal_entry'].add_field(string_fd, 'alloc_name')
event_classes['tensorflowTracer:deallocate_raw_internal_entry'].add_field(string_fd, 'ptr')
event_classes['tensorflowTracer:deallocate_raw_internal_entry'].add_field(int32_fd, 'num_bytes')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'] = btw.EventClass('tensorflowTracer:deallocate_raw_internal_exit')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'].add_field(string_fd, 'alloc_name')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'].add_field(string_fd, 'ptr')
event_classes['tensorflowTracer:deallocate_raw_internal_exit'].add_field(int32_fd, 'num_bytes')

event_classes['tensorflowTracer:do_create_entry'] = btw.EventClass('tensorflowTracer:do_create_entry')
event_classes['tensorflowTracer:do_create_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:do_create_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:do_create_entry'].add_field(string_fd, 'container')
event_classes['tensorflowTracer:do_create_exit'] = btw.EventClass('tensorflowTracer:do_create_exit')
event_classes['tensorflowTracer:do_create_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:do_create_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:do_create_exit'].add_field(string_fd, 'container')
event_classes['tensorflowTracer:do_create_exit'].add_field(uint32_fd, 'success')

event_classes['tensorflowTracer:cleanup_entry'] = btw.EventClass('tensorflowTracer:cleanup_entry')
event_classes['tensorflowTracer:cleanup_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:cleanup_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:cleanup_exit'] = btw.EventClass('tensorflowTracer:cleanup_exit')
event_classes['tensorflowTracer:cleanup_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:cleanup_exit'].add_field(string_fd, 'name')

event_classes['tensorflowTracer:gpu_bfc_alloc_entry'] = btw.EventClass('tensorflowTracer:gpu_bfc_alloc_entry')
event_classes['tensorflowTracer:gpu_bfc_alloc_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:gpu_bfc_alloc_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:gpu_bfc_alloc_entry'].add_field(uint32_fd, 'num_bytes')
event_classes['tensorflowTracer:gpu_bfc_alloc_entry'].add_field(uint32_fd, 'alignment')
event_classes['tensorflowTracer:gpu_bfc_alloc_exit'] = btw.EventClass('tensorflowTracer:gpu_bfc_alloc_exit')
event_classes['tensorflowTracer:gpu_bfc_alloc_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:gpu_bfc_alloc_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:gpu_bfc_alloc_exit'].add_field(uint32_fd, 'num_bytes')
event_classes['tensorflowTracer:gpu_bfc_alloc_exit'].add_field(uint32_fd, 'alignment')

event_classes['tensorflowTracer:gpu_bfc_free_entry'] = btw.EventClass('tensorflowTracer:gpu_bfc_free_entry')
event_classes['tensorflowTracer:gpu_bfc_free_entry'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:gpu_bfc_free_entry'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:gpu_bfc_free_entry'].add_field(int32_fd, 'num_bytes')
event_classes['tensorflowTracer:gpu_bfc_free_exit'] = btw.EventClass('tensorflowTracer:gpu_bfc_free_exit')
event_classes['tensorflowTracer:gpu_bfc_free_exit'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:gpu_bfc_free_exit'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:gpu_bfc_free_exit'].add_field(int32_fd, 'num_bytes')


# Tracepoints : start / end
event_classes['tensorflowTracer:session_start'] = btw.EventClass('tensorflowTracer:session_start')
event_classes['tensorflowTracer:session_start'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:session_start'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:session_start'].add_field(uint32_fd, 'count')
event_classes['tensorflowTracer:session_end'] = btw.EventClass('tensorflowTracer:session_end')
event_classes['tensorflowTracer:session_end'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:session_end'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:session_end'].add_field(uint32_fd, 'count')

event_classes['tensorflowTracer:operation_start'] = btw.EventClass('tensorflowTracer:operation_start')
event_classes['tensorflowTracer:operation_start'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:operation_start'].add_field(string_fd, 'placement')
event_classes['tensorflowTracer:operation_start'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:operation_end'] = btw.EventClass('tensorflowTracer:operation_end')
event_classes['tensorflowTracer:operation_end'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:operation_end'].add_field(string_fd, 'placement')
event_classes['tensorflowTracer:operation_end'].add_field(string_fd, 'name')

event_classes['tensorflowTracer:async_operation_start'] = btw.EventClass('tensorflowTracer:async_operation_start')
event_classes['tensorflowTracer:async_operation_start'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:async_operation_start'].add_field(string_fd, 'placement')
event_classes['tensorflowTracer:async_operation_start'].add_field(string_fd, 'name')
event_classes['tensorflowTracer:async_operation_end'] = btw.EventClass('tensorflowTracer:async_operation_end')
event_classes['tensorflowTracer:async_operation_end'].add_field(string_fd, 'placement')
event_classes['tensorflowTracer:async_operation_end'].add_field(string_fd, 'cat')
event_classes['tensorflowTracer:async_operation_end'].add_field(string_fd, 'name')


# Tracepoints : XY Charts
event_classes['tensorflowTracer:bfc_allocator_stats'] = btw.EventClass('tensorflowTracer:bfc_allocator_stats')
event_classes['tensorflowTracer:bfc_allocator_stats'].add_field(string_fd, 'allocator_name')
event_classes['tensorflowTracer:bfc_allocator_stats'].add_field(uint64_fd, 'num_allocs')
event_classes['tensorflowTracer:bfc_allocator_stats'].add_field(uint64_fd, 'bytes_in_use')
event_classes['tensorflowTracer:bfc_allocator_stats'].add_field(uint64_fd, 'max_bytes_in_use')
event_classes['tensorflowTracer:bfc_allocator_stats'].add_field(uint64_fd, 'max_alloc_size')

event_classes['tensorflowTracer:bfc_chunks_stats'] = btw.EventClass('tensorflowTracer:bfc_chunks_stats')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(string_fd, 'allocator_name')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'total_bytes_in_use')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'total_requested_bytes_in_use')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(int64_fd, 'total_wasted_bytes_in_use')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'total_bytes')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'total_requested_bytes')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(int64_fd, 'total_wasted_bytes')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'chunks')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'in_use_chunks')
event_classes['tensorflowTracer:bfc_chunks_stats'].add_field(uint64_fd, 'free_chunks')


event_classes['tensorflowTracer:bfc_bins_stats'] = btw.EventClass('tensorflowTracer:bfc_bins_stats')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(string_fd, 'allocator_name')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'bin_numero')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'total_chunks_in_bin')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'total_chunks_in_use')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'total_bytes_in_bin')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'total_bytes_in_use')
event_classes['tensorflowTracer:bfc_bins_stats'].add_field(uint64_fd, 'total_requested_bytes_in_use')

event_classes['lttng_python:event'] = btw.EventClass('lttng_python:event')
event_classes['lttng_python:event'].add_field(string_fd, 'asctime')
event_classes['lttng_python:event'].add_field(string_fd, 'msg')
event_classes['lttng_python:event'].add_field(string_fd, 'logger_name')
event_classes['lttng_python:event'].add_field(string_fd, 'funcName')
event_classes['lttng_python:event'].add_field(uint32_fd, 'lineno')
event_classes['lttng_python:event'].add_field(uint32_fd, 'int_loglevel')
event_classes['lttng_python:event'].add_field(uint64_fd, 'thread')
event_classes['lttng_python:event'].add_field(string_fd, 'threadName')


# cuptiTracer
event_classes['cuptiTracer:runtime_api_entry'] = btw.EventClass('cuptiTracer:runtime_api_entry')
event_classes['cuptiTracer:runtime_api_entry'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:runtime_api_entry'].add_field(string_fd, 'name')
event_classes['cuptiTracer:runtime_api_entry'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:runtime_api_exit'] = btw.EventClass('cuptiTracer:runtime_api_exit')
event_classes['cuptiTracer:runtime_api_exit'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:runtime_api_exit'].add_field(string_fd, 'name')
event_classes['cuptiTracer:runtime_api_exit'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:driver_api_entry'] = btw.EventClass('cuptiTracer:driver_api_entry')
event_classes['cuptiTracer:driver_api_entry'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:driver_api_entry'].add_field(string_fd, 'name')
event_classes['cuptiTracer:driver_api_entry'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:driver_api_exit'] = btw.EventClass('cuptiTracer:driver_api_exit')
event_classes['cuptiTracer:driver_api_exit'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:driver_api_exit'].add_field(string_fd, 'name')
event_classes['cuptiTracer:driver_api_exit'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:kernel_begin'] = btw.EventClass('cuptiTracer:kernel_begin')
event_classes['cuptiTracer:kernel_begin'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:kernel_begin'].add_field(string_fd, 'name')
event_classes['cuptiTracer:kernel_begin'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:kernel_end'] = btw.EventClass('cuptiTracer:kernel_end')
event_classes['cuptiTracer:kernel_end'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:kernel_end'].add_field(string_fd, 'name')
event_classes['cuptiTracer:kernel_end'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:kernel_queued'] = btw.EventClass('cuptiTracer:kernel_queued')
event_classes['cuptiTracer:kernel_queued'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:kernel_queued'].add_field(string_fd, 'name')
event_classes['cuptiTracer:kernel_queued'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:memcpy_begin'] = btw.EventClass('cuptiTracer:memcpy_begin')
event_classes['cuptiTracer:memcpy_begin'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:memcpy_begin'].add_field(string_fd, 'name')
event_classes['cuptiTracer:memcpy_begin'].add_field(string_fd, 'details')
event_classes['cuptiTracer:memcpy_begin'].add_field(uint64_fd, 'timestamp')

event_classes['cuptiTracer:memcpy_end'] = btw.EventClass('cuptiTracer:memcpy_end')
event_classes['cuptiTracer:memcpy_end'].add_field(string_fd, 'cat')
event_classes['cuptiTracer:memcpy_end'].add_field(string_fd, 'name')
event_classes['cuptiTracer:memcpy_end'].add_field(string_fd, 'details')
event_classes['cuptiTracer:memcpy_end'].add_field(uint64_fd, 'timestamp')
