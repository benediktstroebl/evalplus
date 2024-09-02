

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if xs == []:
        return []

    # the first term in the derivative is the coefficient of the next term in the original
    first = xs[1:]

    # multiply the first term by the index
    for i in range(len(first)):
        first[i] *= i

    # add the coefficient of the first term
    return [xs[0]] + first

