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
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError(
            "find_zero is only applicable for even number of coefficients with non zero largest coefficient."
        )

    a, b = 0, 1
    while b < len(xs) // 2:
        b *= 2

    while poly(xs, a) * poly(xs, b)!= 0:
        a, b = b, (a + b) // 2

    def ternary_search(low, high, tol=1e-10):
        while abs(high - low) > tol:
            if poly(xs, low) == 0:
                return low
            elif poly(xs, high) == 0:
                return high
            elif poly(xs, low) * poly(xs, high) > 0:
                low = (low + high) // 3
            elif poly(xs, low) * poly(xs, high) < 0:
                high = (low + high) // 3

        return (high + low) / 2

    return ternary_search(a, b)
