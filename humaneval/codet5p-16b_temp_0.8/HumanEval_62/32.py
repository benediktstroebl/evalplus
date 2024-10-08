

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def inner(xs):
        xs[1:] = [i * j for i, j in zip(xs[1:], xs[1:] + [0])]
        return xs
    return list(map(inner, xs))
