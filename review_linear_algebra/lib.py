# -*- encoding: utf-8 -*-
import math
from math import sqrt
from decimal import Decimal, getcontext, DivisionUndefined

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError
        self.coordinates = tuple([Decimal(x) for x in coordinates])
        self.dimension = len(self.coordinates)

    def plus(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def minus(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, c):
        return Vector([Decimal(c) * x for x in self.coordinates])

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, is_degrees=False):
        try:
            cos_val = self.dot(v) / (self.magnitude * v.magnitude)
        except (ZeroDivisionError, DivisionUndefined):
            raise Exception("cannot normalize the zero vector")

        if is_degrees:
            return math.degrees(math.acos(cos_val))
        else:
            return math.acos(cos_val)

    def parallel_with(self, v):
        if self.magnitude * v.magnitude == 0.0:
            return True

        if self.angle_with(v, is_degrees=True) in [0.0, 180.0]:
            return True
        else:
            return False

    def orthogonal_with(self, v):
        if self.magnitude * v.magnitude == 0.0:
            return True

        if self.angle_with(v, is_degrees=True) == 90.0:
            return True
        else:
            return False

    @property
    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sum(coordinates_squared).sqrt()

    @property
    def normalized(self):
        try:
            magnitude = self.magnitude
            return self.times_scalar(Decimal('1.0') / magnitude)
        except ZeroDivisionError:
            raise Exception("cannot normalize the zero vector")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


