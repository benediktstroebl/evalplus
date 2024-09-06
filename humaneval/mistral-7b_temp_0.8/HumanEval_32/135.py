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
    # We take only even number of coefficients
    # since we want to guarantee a solution.
    assert len(xs) % 2 == 0
    # We take largest non-zero coefficient as f(0)
    # to guarantee a solution.
    coeff = xs[0]
    if not coeff:
        raise ValueError('cannot find zero of 0')
    # We subtract x^(len(xs)//2)
    # to make the leading coefficient equal to 1
    # to use quadratic formula.
    xs = [coeff - coeffs for coeffs in xs[1:]]
    assert xs[0] == 1

    # Apply quadratic formula to find x
    # where x is the root.
    x_squared = -(sum(xs[1::2]) / sum(xs[::2]))
    return math.sqrt(x_squared)

