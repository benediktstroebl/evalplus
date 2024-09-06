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
    n = len(xs)
    assert n > 0, "coefficients cannot be empty"
    assert n % 2 == 0, "number of coefficients must be even"
    for i, x in enumerate(xs):
        if x!= 0:
            max_coeff = xs[i]
            max_ind = i
    if max_coeff == 0:
        raise ValueError("no zero point in polynomial")
    for i, x in enumerate(xs):
        if x!= 0 and i!= max_ind:
            x_coeff = xs[i]
            x_ind = i
    y = -xs[max_ind] / (xs[x_ind] - max_coeff)
    if xs[max_ind]!= 0:
        return y
    else:
        raise ValueError("no zero point in polynomial")

