

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if xs == []:
        return xs
    elif xs[0] == 0:
        return []
    elif xs[0] > 0:
        return derivative(xs[1:]) + [xs[0] * len(xs)]
    elif xs[0] < 0:
        return derivative(xs[1:]) + [xs[0] * len(xs)] * -1
    else:
        return []
