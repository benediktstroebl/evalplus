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

    assert len(xs) % 2 == 0, 'len(xs) should be even. xs: {}'.format(xs)
    assert max(xs)!= 0, 'largest non zero coefficient should be non zero. xs: {}'.format(xs)
    # A polynomial is always odd degree.
    assert len(xs) % 2 == 1, 'len(xs) should be odd. xs: {}'.format(xs)
    
    # get number of coefficients
    n = len(xs)
    
    # We use Lagrange's multipliers (also known as non-trivial factors), to find
    # a system of equations. The polynomial is then represented by a polynomial
    # with all but the largest coefficient as a factor.
    # For example:
    # -6 * x^3 + 11 * x^2 - 6 * x + 1
    # is represented by:
    # -6x^3 - 11x^2 - 6x + 1
    
    # By finding the factors we can calculate the point at which poly(x) = 0.
    # That is,
