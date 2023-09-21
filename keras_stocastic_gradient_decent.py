import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import adam_v2

from keras.callbacks import LearningRateScheduler

# Defina a função de taxa de aprendizagem
def cyclical_learning_rate(epoch, lr):
    eta_min = 0.0001
    eta_max = 0.005
    t_cur = epoch % (2 * Ti)
    if t_cur < Ti:
        return eta_min + 0.5 * (eta_max - eta_min) * (1 + np.cos(t_cur / Ti * np.pi))
    else:
        return eta_min + 0.5 * (eta_max - eta_min) * (1 - np.cos((t_cur - Ti) / Ti * np.pi))

# Crie o conjunto de dados fictício
X_train = np.random.rand(100, 10)
y_train = np.random.rand(100, 1)

# Defina os parâmetros da taxa de aprendizagem cíclica
Ti = 5

# Crie o modelo Keras
model = Sequential()
model.add(Dense(64, input_dim=10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile o modelo com a taxa de aprendizagem cíclica
#optimizer = Adam(lr=0.001)
optimizer = adam_v2.Adam(lr=0.001)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
lr_scheduler = LearningRateScheduler(cyclical_learning_rate)
callbacks_list = [lr_scheduler]

# Treine o modelo por 10 épocas
model.fit(X_train, y_train, epochs=10, batch_size=32, callbacks=callbacks_list)
