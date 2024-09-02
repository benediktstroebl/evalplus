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
    if len(xs) % 2 or xs[0] == 0:
        raise ValueError("Not even number of coefficients")

    # multiplication of first 2 elements of list
    # we know first and second elements have opposite sign
    # we know sign of: (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    # multiply by (-6, -11) and add x^2 and x^3
    for i in range(1, len(xs)):
        if xs[i] != 0:
            break
    j = 0
    if xs[i] > 0:
        sign = 1
    else:
        sign = -1
    while j < i:
        xs[j] = xs[j] * sign
        j += 1

    if sign == 1:
        i += 1
    j = len(xs) - 1
    while j > i:
        xs[j] = xs[j] * sign
        j -= 1

    return xs[i]

