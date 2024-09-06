

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # xs[0] + xs[1] * x + xs[2] * x^2 + ....
    # d(xs[0] + xs[1] * x + xs[2] * x^2 + ...) / dx = 1 * d(xs[0])/dx + x * d(xs[1])/dx + x^2 * d(xs[2])/dx + .... = [1, x, x^2, x^3, x^4, x^5, x^6, ...]
    # d(xs[0])/dx = 0
    # d(xs[1])/dx = 1
    # d(xs[2])/dx = 2
    # ....
    # thus, xs[1:]
    return [xs[i] * (i + 1) for i in range(len(xs) - 1)]

