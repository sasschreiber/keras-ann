from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
dataset = numpy.loadtxt("train.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:15360]
Y = dataset[:,15360:15399]

# create model (Dense = fully connected)
model = Sequential()
#input
model.add(Dense(500, input_dim=15360, init='uniform', activation='relu'))
#hidden
#model.add(Dense(8, init='uniform', activation='relu'))
#output
model.add(Dense(39, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, nb_epoch=15, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))