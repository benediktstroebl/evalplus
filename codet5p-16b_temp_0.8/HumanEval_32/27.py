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
        raise ValueError("list xs must have even number of coefficients")
    xs = xs[::-1]
    xs_by_2 = [coeff / 2 for coeff in xs]
    xs_by_2[-1] = xs[-1]
    xs_by_2[-2] = xs[-2] - xs[-1]
    for i in range(len(xs) - 3, -1, -2):
        xs_by_2[i] = xs_by_2[i + 1] - xs_by_2[i + 2]
    return round(-xs_by_2[0] / xs[1], 2)

