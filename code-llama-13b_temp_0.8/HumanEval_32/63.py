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
        raise ValueError('Odd number of coefficients.')

    def _find_zero(xs: list, x: float):
        """
        :param x:
        :return:
        >>> round(_find_zero([1, 2], -0.5), 2) # f(x) = 1 + 2x
        -0.25
        >>> round(_find_zero([1, 2], 0.5), 2) # f(x) = 1 + 2x
        0.0
        """
        if abs(poly(xs, x)) < 1e-10:
            return x
        return _find_zero(xs, x / 2) if poly(xs, x) < 0 else _find_zero(xs, x * 2)

    def _find_first_zero(xs: list, x: float):
        """
        :param x:
        :return:
        >>> round(_find_first_zero([1, 2], -0.5), 2) # f(x) = 1 + 2x
        -0.25
        >>> round(_find_first_zero([1, 2], 0.5), 2) # f(x) = 1 + 2x
        0.0
        """
        left, right = x, x * 2
        if poly(xs, left) * poly(xs, right) < 0:
            return _find_zero(xs, x)
        return _find_first_zero(xs, left) if poly(xs, left) < 0 else _find_first_zero(xs, right)

    return _find_first_zero(xs, 1)

