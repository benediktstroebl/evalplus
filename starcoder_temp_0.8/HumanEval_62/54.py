

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # check that xs has at least two elements
    assert len(xs) > 1
    # init new list for the derivative
    ys = []
    # iterate over the elements of xs except the last one
    for i in range(len(xs) - 1):
        # add to the derivative list the product of the coefficient and the next coefficient
        ys.append(xs[i] * (i + 1))
    return ys

