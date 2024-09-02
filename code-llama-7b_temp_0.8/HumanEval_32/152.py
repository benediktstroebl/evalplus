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
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("list xs should have even number of elements.")
    if xs[n // 2] == 0:
        raise ValueError(f"list xs should have non zero coefficient at n//2 index")

    if n == 2:
        return -xs[1] / (2 * xs[0])

    # This is a generalisation of bisection method
    # to find a zero of a polynomial.
    # Here we can assume that f'(0) != 0
    # so we use x = 0 as a starting point.
    # Then, we do some math to find x_mid which is
    # a midpoint of a bracketing interval [0, x_mid].
    # We then take the midpoint of this interval to be our next guess.

    # derivative = poly(xs[:-1], 0)
    # sign_deriv = math.copysign(1, derivative)
    # x_mid = math.copysign(1, derivative) / (2 * abs(derivative))
    x_mid = -xs[1] / (2 * xs[0])

    # We keep searching for a better x_mid until we reach
    # the precision we want.
    while abs(poly(xs, x_mid)) > 1e-3:
        derivative = poly(xs[:-1], x_mid)
        sign_deriv = math.copysign(1, derivative)
        x_mid = x_mid - sign_deriv * (x_mid - poly(xs, x_mid)) / derivative
    return x_mid

