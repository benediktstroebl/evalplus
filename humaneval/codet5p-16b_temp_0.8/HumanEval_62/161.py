

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    derivative_xs = []
    for x in range(len(xs)):
        if x == 0:
            derivative_xs.append(1)
        else:
            derivative_xs.append(xs[x] * x)
    return derivative_xs
