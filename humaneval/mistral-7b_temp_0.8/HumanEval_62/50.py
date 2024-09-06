

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert len(xs) > 1
    # TODO
    if xs[0] == 0:
        return [0]
    else:
        n = len(xs)
        n_1 = len(xs) - 1
        return [xs[1] + xs[2] * n + xs[n_1] * n_1] + derivative(xs[1:])

