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
    assert len(xs) % 2 == 0
    # Assuming that xs is even and non-zero
    n = len(xs) // 2
    # Found all nth zero, so we get x_n
    x = [xs[i] for i in range(n, -1, -1)]
    # Reverse x so we get x_n+1 = x_n - f(x_n) / f'(x_n)
    x.reverse()
    return sum(x) / sum([coeff * (math.pow(x[i], i + 1)) for i, coeff in enumerate(x)])

