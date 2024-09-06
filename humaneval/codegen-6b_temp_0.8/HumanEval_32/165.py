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
    if len(xs) % 2 != 0 or max(xs) == 0:
        raise ValueError("find_zero: only poly(x) = 0 for even length list of coefficients")
    if xs[0] == 0:
        return 0
    if len(xs) == 2:
        return -xs[1] / xs[0]
    if len(xs) == 4:
        return -sum([x * xs[i] for i, x in enumerate(xs[1:] + [0])]) / sum(xs[1:])
    if len(xs) == 6:
        # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
        # check sign
        if xs[2] * xs[-1] > 0 and xs[1]/xs[-1] > 0:
            y = xs[2] / xs[-1]
        elif xs[2] * xs[-1] < 0 and xs[1]/xs[-1] < 0:
            y = -xs[2] / xs[-1]
        else:
            y = -xs[1] / xs[-1]
        # check for same sign
        if xs[2] * xs[-2] > 0 and xs[1] / xs[-2] > 0:
            z = xs[2] / xs[-2]
        elif xs[2] * xs[-2] < 0 and xs[1] / xs[-2] < 0:
            z = -xs[2] / xs[-2]
        else:
            z = -xs[1] / xs[-2]
        t = sum(xs[1:]) / (len(xs) - 1)
        return -sum([x * (z + y * t) for x, y in zip(xs[1:-2], (xs[2:] + [0, 0])[:-1])]) / sum(xs[1:-2])
    raise ValueError("input data should have even length but has length: {