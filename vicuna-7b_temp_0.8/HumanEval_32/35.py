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
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have an even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("Last coefficient should be non-zero")

    xs_neg = xs[:-1]
    neg_x_roots = [-math.pow(x, -1) for x in xs_neg]
    x_roots = []

    for x in xs_neg:
        coef = 1
        for i in range(len(xs_neg)):
            coef *= x
            if coef == 0:
                x_roots.append(x)
                break

    for x in xs_neg:
        if x ** len(xs_neg) == 1:
            x_roots.append(x)

    for x in x_roots:
        if poly(x_roots, x) == 0:
            return x

