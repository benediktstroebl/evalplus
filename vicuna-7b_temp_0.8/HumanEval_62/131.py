

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    n = len(xs)
    ret = [0] * (n+1)
    for i in range(1, n):
        ret[i] = xs[i-1]
    for i in range(2, n):
        ret[i] = ret[i-1] + xs[i-2]
    return ret
