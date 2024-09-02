

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    xs.reverse()
    derivative_xs = []
    for i in range(len(xs) - 1):
        derivative_xs.append(xs[i + 1] * (i + 1))
    derivative_xs.reverse()
    return derivative_xs
