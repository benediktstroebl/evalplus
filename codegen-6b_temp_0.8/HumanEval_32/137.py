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
    coeffs = xs[:]
    coeffs.insert(0, 0)
    # coeffs.insert(0, 1)
    xs = coeffs[1:]
    del coeffs
    deg = len(xs) - 1
    sign = 1
    for i in range(deg, 0, -2):
        if sign < 0:
            break
        for j in range(i - 1, -1, -1):
            A = xs[j]
            B = xs[i - 1]
            if A != 0:
                xs.append(round(-(B / A), 2))
                sign = sign * -1
                break
    A = xs[-1]
    del xs[-1]
    return A

