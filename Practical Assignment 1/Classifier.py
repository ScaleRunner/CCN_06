import numpy as np
import chainer
from chainer import cuda, Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions

class Classifier(Chain):
    def __init__(self, predictor):
        super(Classifier, self).__init__()
        with self.init_scope():
            self.predictor = predictor

    def __call__(self, data, labels):
        y = self.predictor(data)
        self.loss = F.softmax_cross_entropy(y, labels)
        self.accuracy = F.accuracy(y, labels)
        report({'loss': self.loss, 'accuracy': self.accuracy}, self)
        return self.loss
