

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # reverse the list
    # zip the reversed list with an index, i
    # then reverse again
    return [x * i for i, x in zip(range(len(xs), 0, -1), reversed(xs[1:]))]

