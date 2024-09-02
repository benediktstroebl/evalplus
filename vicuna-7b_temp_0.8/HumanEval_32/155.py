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
    n = len(xs) // 2
    zero = [0] * n
    for i in range(1, n):
        for j in range(i):
            for k in range(i + 1, n):
                if xs[i] * xs[j] == 0:
                    break
            if xs[i] != 0:
                zero[i] = -xs[i] / xs[j]
    if len(zero) == 1:
        return zero[0]
    if len(zero) == 2:
        return min(zero[0], zero[1])
    else:
        return 0

