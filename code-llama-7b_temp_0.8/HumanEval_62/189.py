

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return []
    if len(xs) == 2:
        return [xs[1]]
    if len(xs) == 3:
        return [2 * xs[1], xs[2]]
    if len(xs) == 4:
        return [2 * xs[1], 4 * xs[2], xs[3]]
    return [x + 2 * xs[i] for i, x in enumerate(xs[1:])]

