# devices available
# ['/cpu:0', '/device:SYCL:0']

from __future__ import print_function

import tensorflow as tf
import numpy as np
import datetime
import time
from tensorflow.python.client import timeline
import socket
host = socket.gethostname()

start_time = time.time()


# import data
x_set = np.array([]).reshape(0, 32, 32, 3)
y_set = np.array([]).reshape(0, 2)
for it in range(1):
    x_tmp = np.load("/home/pierre/dev/projet_inf8225/data/32_large/xtrain_32_" + str(it) + ".dat")
    y_tmp = np.load("/home/pierre/dev/projet_inf8225/data/32_large/ytrain_32_" + str(it) + ".dat")
    # x_tmp = np.load("/home/pierre/dev/32_large/xtrain_32_" + str(it) + ".dat")
    # y_tmp = np.load("/home/pierre/dev/32_large/ytrain_32_" + str(it) + ".dat")
    x_set = np.append(x_set, x_tmp, axis=0)
    y_set = np.append(y_set, y_tmp, axis=0)

# create train, valid and test set
trainSize = int(x_set.shape[0] * 0.7)
validSize = int(x_set.shape[0] * 0.15)

x_train = x_set[:trainSize]
y_train = y_set[:trainSize]
x_val = x_set[trainSize:trainSize+validSize]
y_val = y_set[trainSize:trainSize+validSize]
x_test = x_set[trainSize+validSize:]
y_test = y_set[trainSize+validSize:]

# Parameters
learning_rate = 0.001
training_epochs = 1
batch_size = 32
nb_batch = int(x_train.shape[0]/batch_size)

# Network Parameters
img_size = 32
n_classes = 2
dropout = 1 # Dropout, probability to keep units


# tf Graph input
x = tf.placeholder(tf.float32, [None, img_size, img_size, 3])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


# Create some wrappers for simplicity
def conv2d(x, W, b, strides=1):
    # Conv2D wrapper, with bias and relu activation
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)

def maxpool2d(x, k=2):
    # MaxPool2D wrapper
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='SAME')

# Create model
def conv_net(x, weights, biases, dropout):
    # Reshape input picture
    x = tf.reshape(x, shape=[-1, img_size, img_size, 3])
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    conv1 = conv2d(conv1, weights['wc2'], biases['bc2'])
    conv1 = maxpool2d(conv1, k=2)
    conv1 = tf.nn.dropout(conv1, dropout)

    # Fully connected layer
    fc1 = tf.reshape(conv1, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    fc2 = tf.nn.dropout(fc1, dropout)
    # Output, class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out


# Store layers weight & bias
weights = {
    'wc1': tf.Variable(tf.random_normal([5, 5, 3, 32])),
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),

    'wd1': tf.Variable(tf.random_normal([16*16*64, 100])),
    'out': tf.Variable(tf.random_normal([100, n_classes]))
}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),

    'bd1': tf.Variable(tf.random_normal([100])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = conv_net(x, weights, biases, keep_prob)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()


# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
    run_metadata = tf.RunMetadata()

    for epoch in range(training_epochs):
        for i in range(nb_batch):
            batch_x = x_train[i*batch_size:(i+1)*batch_size]
            batch_y = y_train[i*batch_size:(i+1)*batch_size]
            # Run optimization op (backprop)
            _ = sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,
                                               keep_prob: dropout}, options=run_options, run_metadata=run_metadata)
        # Calculate batch loss and accuracy
        loss, acc = sess.run([cost, accuracy], feed_dict={x: x_val,
                                                          y: y_val,
                                                          keep_prob: 1.})
        print("Epoch (" + str(epoch) + ") Minibatch Loss= " + "{:.6f}".format(loss) + ", Training Accuracy= " + "{:.5f}".format(acc))

    print("Optimization Finished!")
    res = sess.run(correct_pred, feed_dict={x: x_test, y: y_test, keep_prob: 1})
    loss, acc = sess.run([cost, accuracy], feed_dict={x: x_test,
                                                      y: y_test,
                                                      keep_prob: 1.})
    print(res)
    print("Accuracy : %f\n" % acc)

elapsed_time = time.time() - start_time
print("Elapsed time :", elapsed_time)
# Create the Timeline object, and write it to a json
tl = timeline.Timeline(run_metadata.step_stats)
ctf = tl.generate_chrome_trace_format()
with open('trace_' + __file__[:-3] + "_" + host + '.json', 'w') as f:
        f.write(ctf)
