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

    def poly_derivative(xs: list):
        """ xs are coefficients of a polynomial.
        returns coefficients of polynomial derivative.
        >>> poly_derivative([0, 1])
        [1]
        >>> poly_derivative([-1, 0, 3])
        [3, -1]
        >>> poly_derivative([0, -2, 1, -3])
        [-2, 3, -1]
        """
        return [i * j for i, j in zip(xs[1:], range(1, len(xs)))]

    def polynomial_root(xs: list):
        """ xs are coefficients of a polynomial.
        finds a root of the polynomial.
        >>> round(polynomial_root([1, 2]), 2)
        -0.5
        >>> round(polynomial_root([-3, 0, 1]), 2)
        1.0
        >>> round(polynomial_root([1, 0, 0, 0, -6, 11, -6, 1]), 2)
