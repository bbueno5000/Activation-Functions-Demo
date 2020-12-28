"""
TODO: docstring
"""
import numpy

class ActivationFunctions:
    """
    TODO: docstring
    """
    def arctan(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            return (numpy.cos(x) ** 2)
        return numpy.arctan(x)

    def gaussian(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            for i in range(len(x)):
                for k in range(len(x[i])):
                    x[i][k] = -2 * x[i][k] * numpy.exp(-x[i][k] ** 2)
        for i in range(len(x)):
            for k in range(len(x[i])):
                x[i][k] = numpy.exp(-x[i][k] ** 2)
        return x

    def relu(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            for i in range(len(x)):
                for k in range(len(x[i])):
                    if x[i][k] > 0:
                        x[i][k] = 1
                    else:
                        x[i][k] = 0
            return x
        for i in range(len(x)):
            for k in range(len(x[i])):
                if x[i][k] > 0:
                    pass
                else:
                    x[i][k] = 0
        return x

    def sigmoid(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            return x * (1 - x)
        return 1 / (1 + numpy.exp(-x))

    def squash(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            for i in range(len(x)):
                for k in range(len(x[i])):
                    if x[i][k] > 0:
                        x[i][k] = (x[i][k]) / (1 + x[i][k])
                    else:
                        x[i][k] = (x[i][k]) / (1 - x[i][k])
            return x
        for i in range(len(x)):
            for k in range(len(x[i])):
                x[i][k] = (x[i][k]) / (1 + abs(x[i][k]))
        return x

    def step(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            for i in range(len(x)):
                for k in range(len(x[i])):
                    if x[i][k] > 0:
                        x[i][k] = 0
            return x
        for i in range(len(x)):
            for k in range(len(x[i])):
                if x[i][k] > 0:
                    x[i][k] = 1
                else:
                    x[i][k] = 0
        return x

    def tanh(self, x, derivative=False):
        """
        TODO: docstring
        """
        if derivative:
            return 1 - (x ** 2)
        return numpy.tanh(x)
