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
    a = xs[0]
    b = xs[1]
    c = xs[2]
    d = xs[3]

    def discriminant(a, b, c, d):
        return 18 * a * c * b * d - 4 * b**3 * c**2 - 27 * a**2 * d**2

    if discriminant(a, b, c, d) < 0:
        return None
    else:
        u = -b / (2 * a)
        v = math.sqrt(discriminant(a, b, c, d) / (4 * a**3))
        x1 = u + v
        x2 = u - v

        def f(x):
            return poly([a, b, c, d], x)

        if f(x1) == 0:
            return x1
        elif f(x2) == 0:
            return x2
        else:
            return None

