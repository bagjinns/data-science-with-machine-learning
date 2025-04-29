import tensorflow as tf

# tensor1 = tf.constant([3, 4, 5])
# tensor2 = tf.constant([6, 7, 8])
# # print(tensor1 + tensor2)


# tensor3 = tf.constant([[1, 2],
#                       [3, 4]])


# w = tf.Variable(1.0)
# print(w.numpy())
# w.assign(2.0)
# print(w.numpy())


height = 170
shose_size = 260

# shose_size = height * a + b

def loss_function():
    return tf.square(260 - (height * a + b))

a = tf.Variable(0.3)
b = tf.Variable(0.1)


opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(loss_function, var_list = [a, b])
    print(a, b)