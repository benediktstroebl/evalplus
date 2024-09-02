import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    def same_sign(a, b):
        return a * b > 0

    def find_root(xs: list):
        # find minimum and maximum of xs
        if xs[0] == 0:
            return 0
        min_x = 0
        for i in range(1, len(xs)):
            if xs[i]!= 0 and same_sign(xs[i - 1], xs[i]):
                min_x = i
        max_x = len(xs) - 1
        for i in range(len(xs) - 2, -1, -1):
            if xs[i]!= 0 and same_sign(xs[i + 1], xs[i]):
                max_x = i
        # use bisection method
        x = (min_x + max_x) / 2
        while max_x - min_x > 1:
            if poly(xs, x) == 0:
                return x
            elif poly(xs, min_x) * poly(xs, x) > 0:
                min_x = x
            else:
                max_x = x
            x = (min_x + max_x) / 2
        return min_x

    return find_root(xs)

