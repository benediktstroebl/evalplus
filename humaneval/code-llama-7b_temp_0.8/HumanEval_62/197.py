

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # add your own doctests, or my tests
    # will check that you have implemented the function correctly.

    if xs == []:
        return []

    # for this return [1, 4, 12, 20]
    if len(xs) == 1:
        return []

    # for this return [1, 4, 12]
    if len(xs) == 2:
        return [xs[1]]

    # for this return [2, 6]
    if len(xs) == 3:
        return [xs[1], 2 * xs[2]]

    return [xs[1]] + 2 * xs[2:]


