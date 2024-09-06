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
    poly = poly

    def sub_poly(xs: list, x: float):
        """
        Helper function to find_zero.
        """
        xs = xs[1:]
        return poly(xs, x)

    def binary_search(xs: list, l: float, r: float, tol: float = 0.0001):
        """
        binary search for root of a polynomial of even degree.
        """
        if r - l < tol:
            return l
        m = (l + r) / 2
        if sub_poly(xs, m) * sub_poly(xs, m - tol):
            return binary_search(xs, l, m - tol, tol)
        return binary_search(xs, m + tol, r, tol)

    assert len(xs) % 2 == 0 and xs[0] != 0
    return binary_search(xs, -math.inf, math.inf)
