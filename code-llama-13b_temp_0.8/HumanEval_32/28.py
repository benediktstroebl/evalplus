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
    assert len(xs) % 2 != 0
    assert max(xs) != 0
    # If f(x) = a0 + a1 * x + ... + an * x^n, then f'(x) = a1 + 2 * a2 * x + ... + n * an * x^n - 1
    # Setting f'(x) = 0 we can find f'(x0) = 0 by solving
    # a1 + 2 * a2 * x0 + ... + n * an * x0^n - 1 = 0
    # and x0 is a root of f(x)
    # As a result, we can find a solution of f(x) = 0 by solving
    # f'(x0) = 0
    derivative = [i * xs[-1] for i in xs[1:-1]]
    return find_zero(derivative)
