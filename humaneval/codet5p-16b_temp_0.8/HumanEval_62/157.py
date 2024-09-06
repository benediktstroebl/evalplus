

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    xs[0] = derivative_x0(xs)
    xs[1] = derivative_x1(xs)
    xs[2] = derivative_x2(xs)
    xs[3] = derivative_x3(xs)
    return xs

