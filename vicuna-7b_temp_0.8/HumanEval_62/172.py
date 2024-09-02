

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    x_coeff = []
    for x in xs:
        if x not in x_coeff:
            x_coeff.append(x)
        for y in x_coeff:
            if y % 2 == 0:
                x_coeff.remove(y)
    derivative = []
    for i in x_coeff:
        derivative.append(i // 2)
    return derivative
