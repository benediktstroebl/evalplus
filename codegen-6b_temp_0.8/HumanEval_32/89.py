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
    # First find the degree of the polynomial
    n = len(xs) // 2
    # First find the first non-zero coefficient
    first_non_zero = _first_non_zero_index(xs, n)  # Equivalent to find_zero_index(xs, 0, n)
    # Convert to the correct format for polynomial
    zero_power_set = _get_zero_power_set(first_non_zero, n)
    # Evaluate the polynomial
    return _first_zero(xs, zero_power_set)

