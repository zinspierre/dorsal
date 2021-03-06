from __future__ import print_function

import tensorflow as tf
from tensorflow.python.client import timeline
import socket
host = socket.gethostname()

run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE, output_partition_graphs=True)
run_metadata = tf.RunMetadata()

"""
# Basic constant operations
# The value returned by the constructor represents the output
# of the Constant op.
a = tf.constant(2, name="a")
b = tf.constant(3, name="b")


# Launch the default graph.
with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition with constants: %i" % sess.run(a+b, options=run_options, run_metadata=run_metadata))
    print("Multiplication with constants: %i" % sess.run(a*b, options=run_options, run_metadata=run_metadata))

# Basic Operations with variable as graph input
# The value returned by the constructor represents the output
# of the Variable op. (define as input when running session)
# tf Graph input
a = tf.placeholder(tf.int16, name="a")
b = tf.placeholder(tf.int16, name="b")

# Define some operations
add = tf.add(a, b, "add")
mul = tf.multiply(a, b, "mul")

# Launch the default graph.
with tf.Session() as sess:
    # Run every operation with variable input
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}, options=run_options, run_metadata=run_metadata))
    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}, options=run_options, run_metadata=run_metadata))

"""

# ----------------
# More in details:
# Matrix Multiplication from TensorFlow official tutorial

a = tf.placeholder(tf.int32, name="a", shape=(1,1))
b = tf.placeholder(tf.int32, name="b", shape=(1,1))

# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(a, b)

# To run the matmul op we call the session 'run()' method, passing 'product'
# which represents the output of the matmul op.  This indicates to the call
# that we want to get the output of the matmul op back.
#
# All inputs needed by the op are run automatically by the session.  They
# typically are run in parallel.
#
# The call 'run(product)' thus causes the execution of threes ops in the
# graph: the two constants and matmul.
#
# The output of the op is returned in 'result' as a numpy `ndarray` object.
with tf.Session() as sess:
    result = sess.run(product, feed_dict={a: [[1.]], b: [[10.]]}, options=run_options, run_metadata=run_metadata)
    print(result)
    # ==> [[ 12.]]


"""
# ----------------
# More in details:
# Matrix Multiplication from TensorFlow official tutorial

# Create a Constant op that produces a 1x2 matrix.  The op is
# added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
matrix1 = tf.constant([[3., 3.]])

# Create another Constant that produces a 2x1 matrix.
matrix2 = tf.constant([[2.],[2.]])

# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(matrix1, matrix2)

# To run the matmul op we call the session 'run()' method, passing 'product'
# which represents the output of the matmul op.  This indicates to the call
# that we want to get the output of the matmul op back.
#
# All inputs needed by the op are run automatically by the session.  They
# typically are run in parallel.
#
# The call 'run(product)' thus causes the execution of threes ops in the
# graph: the two constants and matmul.
#
# The output of the op is returned in 'result' as a numpy `ndarray` object.
with tf.Session() as sess:
    result = sess.run(product, options=run_options, run_metadata=run_metadata)
    print(result)
    # ==> [[ 12.]]
"""

# Create the Timeline object, and write it to a json
tl = timeline.Timeline(run_metadata.step_stats)
ctf = tl.generate_chrome_trace_format(show_memory=True)
sess.close()
with open('trace_' + __file__[:-3] + "_" + host + '.json', 'w') as f:
        f.write(ctf)
