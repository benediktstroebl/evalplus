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
    assert len(xs) % 2 == 0, "find_zero requires list xs having even number of coefficients"
    xs = list(reversed(xs))  # list xs has even number of coefficients
    while xs[0] == 0:  # ignore leading zeros
        xs = xs[1:]
    while xs[-1] == 0:  # ignore trailing zeros
        xs = xs[:-1]
    for i, coeff in enumerate(xs):
        if coeff!= 0:
            break
    d = (i + 1) // 2  # degree of the polynomial
    roots = []
    for i in range(d):
        root = - xs[2 * i + 1] / (2 * xs[2 * i])  # roots[i] is a root of f'(x) = 0
        if root not in roots:
            roots.append(root)
    roots = sorted(roots)  # roots[0] is the smallest
    return roots[0]
