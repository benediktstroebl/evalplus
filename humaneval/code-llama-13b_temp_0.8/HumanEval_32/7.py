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
    # 1. make sure that len(xs) is even
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even")
    # 2. make sure that xs is not all 0
    if len([coeff for coeff in xs if coeff != 0]) == 0:
        raise ValueError("There is no zero")
    # 3. find approximate x (i.e. x0)
    x0 = 1.0
    while True:
        # check if we already found a zero
        if abs(poly(xs, x0)) < 1e-5:
            return x0
        # update x0
        x0 = (x0 + poly(xs, x0)) / 2

