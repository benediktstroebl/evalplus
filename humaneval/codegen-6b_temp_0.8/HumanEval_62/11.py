

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert len(xs) >= 1, "Coefficients list must have at least one element"
    # TODO: Bonus - Override this implementation with the help of numpy.
    #       See https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyder.html
    for i in range(len(xs)-1):
        xs[i+1] = xs[i] * (len(xs) - i - 1)
    return xs[1:]
