

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # TODO: implement the function
    deriv = []
    for i in range(0, len(xs)):
        if i == 0:
            deriv.append(xs[0])
        else:
            deriv.append(xs[i] * i)
    return deriv


