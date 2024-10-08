

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = [0]
    for i, x in enumerate(xs):
        if i != 0:
            result.append(xs[i-1] * i)
        else:
            result.append(xs[i])
    return result[1:]
