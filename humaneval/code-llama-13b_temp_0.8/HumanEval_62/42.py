

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def mul(x, i):
        return i * x
    def mul_by_index(i):
        return lambda x: i * x
    indices = range(1, len(xs))
    derivatives = list(map(mul_by_index, indices))
    dxs = list(map(mul, xs, derivatives))
    dxs = dxs[1:]
    return dxs

