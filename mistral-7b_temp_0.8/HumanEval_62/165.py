

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if not xs:
        return []
    if len(xs) == 1:
        return [0]
    xs_0, xs_1 = xs[:-1], xs[1:]
    return [x + y * 2 for x, y in zip(xs_0, xs_1)] + [xs[-1]]
