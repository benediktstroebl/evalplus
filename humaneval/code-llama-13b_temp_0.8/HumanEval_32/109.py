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
    assert len(xs) % 2 == 0, "Number of coefficients must be even."
    assert max(xs) != 0, "Largest non zero coefficient must not be zero"

    # xs[i] * x^i
    xs = [coeff * math.pow(0, i) for i, coeff in enumerate(xs)]

    # polynomial is monotonically increasing for x > -1/2 * xs[1] / xs[0]
    x_low = -.5 * xs[1] / xs[0]

    # polynomial is monotonically decreasing for x < -1/2 * xs[1] / xs[0]
    x_high = 2

    # binary search to find zero.
    while abs(x_high - x_low) > 1e-10:
        x_mid = (x_high + x_low) / 2
        if poly(xs, x_mid) * poly(xs, x_low) <= 0:
            x_high = x_mid
        else:
            x_low = x_mid

    return x_low

