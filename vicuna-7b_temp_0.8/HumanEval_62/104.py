

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
        return [0, 0, 0]
    if len(xs) == 1:
        return [xs[0], 0, 0]
    result = [0, 0, 0]
    for x in xs[1:]:
        result = [a*x + b for a, b in zip(result, xs)]
    return result