# One variable multi-step forecast with Keras CNN
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D

from numpy.random import seed
seed(42)
import tensorflow as tf
tf.random.set_seed(2)


def split_sequence(sequence, n_steps_in, n_steps_out):
    '''
splits the one dimensional input sequence into training samples
    '''
    X = list()
    y = list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        # check if we are beyond the sequence
        if out_end_ix > len(sequence):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

raw_seq = [780.3,1018.0,1349.0,	3026.0,	4279.0,	4447.0,	4755.0,	4856.0,	4583.0,	4408.0,	4664.0,	6608.0,	7017.0,	7500.0,	6489.0,	7660.0]

#Choose the number of observations, n_steps_in to consider when forecasting n_steps_out
n_steps_in, n_steps_out = 6, 5


# split into samples
X, y = split_sequence(raw_seq, n_steps_in, n_steps_out)
print(X)
print(y)
# reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
# define model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_steps_in, n_features)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(n_steps_out))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=2000, verbose=0)
# demonstrate prediction
x_input = array([4664.0,6608.0,	7017.0,	7500.0,	6489.0,	7660.0])
x_input = x_input.reshape((1, n_steps_in, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)
