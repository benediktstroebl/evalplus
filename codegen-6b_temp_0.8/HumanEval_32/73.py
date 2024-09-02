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
    # find first non zero coefficient
    for i, coeff in enumerate(xs):
        if coeff != 0:
            zero_point = i
            break
    else:
        return None

    # find real roots
    roots = []
    for i in range(zero_point, len(xs), 2):
        if xs[i] != 0:
            root = -coeff / xs[i]
            roots.append(root)

    # no real roots, try to find approximation
    if len(roots) == 0:
        approx = xs[zero_point]
        if approx > 0:
            root = -approx / xs[zero_point + 1]
        else:
            root = approx / xs[zero_point - 1]

        roots.append(root)
    return min(roots)

