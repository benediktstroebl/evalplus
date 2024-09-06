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

    def find_pos_root(xs: list):
        """
        find_pos_root return the position of the first root
        in the positive half plane.
        >>> find_pos_root([1, 1, -2])
        1
        >>> find_pos_root([-1, -1, -2])
        2
        """
        return next(i for i, val in enumerate(xs) if val >= 0)

    root_pos = find_pos_root(xs)

    def roots_count(xs: list):
        """
        roots_count returns the number of roots in the positive half plane
        of a polynomial of even degree with coefficients xs
        """
        return xs.count(0) // 2

    if roots_count(xs) == 0:
        raise ValueError("Root not found")
    elif roots_count(xs) == 1:
        return xs[root_pos]

    def diff_poly(xs: list, x: float):
        """
        diff_poly returns the derivative of polynomial of even degree with
        coefficients xs at point x.
        diff_poly assumes that xs is differentiable.
        """
        return sum([i * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

    def secant(x0: float, x1: float, tol: float = 1e-10):
        """
        secant finds a zero of polynomial using the secant method.
        >>> secant(1, 2)
        1.61803398875
        """
        while abs(x1 - x0) > tol:
            x0 = x1
            x1 = x1 - poly(xs, x1) / diff_poly(xs, x1)

        return x1

    x0 = xs[root_pos]
    x1 = xs[root_pos + 1]
    return secant(x0, x1)

