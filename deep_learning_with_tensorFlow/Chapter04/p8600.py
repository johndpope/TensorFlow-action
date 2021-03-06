import tensorflow as tf

TRAINING_STEPS = 100
global_step = tf.Variable(0)
# 目前还是没有太明白
# decayed_learning_rate = learning_rate * decay_rate ^ (global_step / decay_steps)
# exponential_decay(learning_rate, global_step, decay_steps, decay_rate, staircase=False, name=None)
# decayed_learning_rate 为每一轮优化时 使用的学习率
# learning_rate 事先设置的初始化学习率
# decay_rate 衰减系数
# decay_steps 衰减系数
# global_step: A scalar `int32` or `int64` `Tensor` or a Python number.
#      Global step to use for the decay computation.  Must not be negative.
# global_step: Optional `Variable` to increment by one after the
#         variables have been updated.
# LEARNING_RATE 中的global_step 初始值为0 通过minimize 进行 自增长 中的global_step
LEARNING_RATE = tf.train.exponential_decay(0.1, global_step, 1, 0.96, staircase=True)

x = tf.Variable(tf.constant(5, dtype=tf.float32), name="x")
y = tf.square(x)
train_op = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(y, global_step=global_step)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(TRAINING_STEPS):
        sess.run(train_op)
        if i % 10 == 0:
            LEARNING_RATE_value = sess.run(LEARNING_RATE)
            x_value = sess.run(x)
            print('global_step：', sess.run(global_step))
            print(
                "After %s iteration(s): x%s is %f, learning rate is %f." % (i + 1, i + 1, x_value, LEARNING_RATE_value))
