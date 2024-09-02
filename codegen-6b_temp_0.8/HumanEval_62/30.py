

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert len(xs) > 0
    deriv = []
    for i in range(len(xs)):
        if i == 0:
            deriv.append(xs[i+1])
        elif i == len(xs)-1:
            deriv.append(xs[i])
        else:
            deriv.append(xs[i] + xs[i+1])

    return deriv

