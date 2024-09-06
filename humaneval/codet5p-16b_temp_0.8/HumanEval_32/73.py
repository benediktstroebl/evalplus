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

    if len(xs) % 2!= 0:
        raise ValueError("We can't find zero for odd number of coeffcients.")

    if len(xs) == 2:
        x = -xs[1] / xs[0]
        return x if abs(x) > 1e-12 else 0

    s_1 = sum([abs(coeff) for coeff in xs])
    s_2 = sum([coeff * coeff for coeff in xs])

    c = -s_1 / s_2
    # f(x) = x1 + x2 * c
    # find x such that f(x) = 0
    # f(x) = a_1 + a_2 * x + a_3 * x^2 +.... a_n * x^n
    a_n = xs[-1]
    a_n_1 = xs[-2]
    d = a_n * a_n_1 * c
    if d == 0:
        return 0
    x1 = (-a_n_1 - math.sqrt(d))
