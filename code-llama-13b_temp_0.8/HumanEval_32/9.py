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
        raise ValueError(
            "find_zero can only be applied to polynomials of even degree"
        )

    def iterate(a, b):
        if abs(b - a) < 1e-4:
            return (a + b) / 2
        else:
            x = (a + b) / 2
            fx = poly(xs, x)
            if fx == 0:
                return x
            elif fx * xs[0] > 0:
                return iterate(x, b)
            else:
                return iterate(a, x)

    return iterate(-10000, 10000)

