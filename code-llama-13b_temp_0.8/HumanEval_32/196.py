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
    if len(xs) == 1:
        return -xs[0] / xs[0]

    def _find_zero(xs: list, x_l: float, x_h: float):
        f_l = poly(xs, x_l)
        f_h = poly(xs, x_h)
        if f_l * f_h <= 0:
            return x_l if abs(f_l) < abs(f_h) else x_h
        else:
            m = (x_l + x_h) / 2
            f_m = poly(xs, m)
            if f_m * f_l <= 0:
                return _find_zero(xs, x_l, m)
            else:
                return _find_zero(xs, m, x_h)

    return _find_zero(xs, 0, 1)
