

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
        return [0]
    xs_len = len(xs)
    result = [0] * (xs_len + 1)
    for i, x in enumerate(xs):
        j = i + 1
        while j < xs_len:
            result[j] += x
            j += 1
    return result
