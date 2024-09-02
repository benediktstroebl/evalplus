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
    if len(xs) % 2 == 1:
        raise ValueError("find_zero only takes list having even number of elements")
    # find a largest non zero coefficient
    # find_zero takes max instead of max_by because max_by is lazy.
    # and lazy evaluation of max is expensive.
    coeff_max = max(xs)
    if coeff_max == 0:
        raise ValueError("find_zero only takes list having non zero elements")
    n = int(len(xs) / 2)
    # coeffs are the coefficients of (x - z) * (x - z)...
    coeffs = [x for i, x in enumerate(xs) if (i // n) % 2 == 1]
    return find_zero(coeffs) + find_zero([coeff_max])

