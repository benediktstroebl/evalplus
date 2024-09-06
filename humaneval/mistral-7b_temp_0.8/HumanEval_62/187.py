

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # 3 * x^2 + 5 * x^1 + 7 * x^0 = 3 * (x^2 + 5 * x + 7)
    # 2 * x^3 + 6 * x^2 + 10 * x^1 + 15 * x^0 = 2 * (x^3 + 6 * x^2 + 10 * x + 15)
    # 2 * x^3 + 10 * x^2 + 30 * x^1 + 60 * x^0 = 2 * (x^3 + 10 * x^2 + 30 * x + 60)
    # 2 * x^3 + 6 * x^2 + 15 * x^1 + 30 * x^0 = 2 * (x^3 + 6 * x^2 + 15 * x + 30)
    # 2 * x^3 + 15 * x^2 + 45 * x^1 + 90 * x^0 = 2 * (x^3
