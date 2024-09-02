

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert isinstance(xs, list)
    assert len(xs) > 0
    k = len(xs) - 1
    p = [0] * (k + 1)
    for i in range(k + 1):
        if i == 0:
            p[k - i] = xs[k]
        elif i == k:
            p[k - i] = -1 * xs[k - i]
        else:
            p[k - i] = xs[k - i] * (k - i)
    return p

