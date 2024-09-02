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
    n = len(xs)
    assert n % 2 == 0
    assert abs(xs[-1]) < 1e-10
    if n == 2:
        return -b / a
    if n == 4:
        c, d, e, _ = xs
        return (-d + math.sqrt(d**2 - 4 * a * c)) / (2 * a)
    if n == 6:
        c, d, e, f, g, h = xs
        return ((-2 * d + math.sqrt(4 * a * c + 4 * a * d - 4 * b * c - 8 * c * e + 4 * b * e - 4 * a * f + 4 * c * f - 4 * b * g - 4 * a * h)) / (4 * a)
                - (-2 * d - math.sqrt(4 * a * c + 4 * a * d - 4 * b * c - 8 * c * e + 4 * b * e - 4 * a * f + 4 * c * f - 4 * b * g - 4 * a * h)) / (4 * a))

