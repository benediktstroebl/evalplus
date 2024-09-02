

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert isinstance(xs, list) and len(xs) >= 2
    ys = xs[1:]
    ys.append(0)
    for i in range(1, len(ys)):
        ys[i] = ys[i-1] * (i-1)
    return ys
