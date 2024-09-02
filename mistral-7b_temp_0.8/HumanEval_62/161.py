

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = []
    for i in range(len(xs) - 1):
        x = xs[i]
        next = xs[i + 1]
        result.append(next * (i + 1))
    result.append(xs[0])
    return result
