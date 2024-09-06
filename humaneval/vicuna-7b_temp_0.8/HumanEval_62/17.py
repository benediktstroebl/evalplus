

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    coeffs = [float(x) for x in xs]
    d = [0] * len(xs)
    for i in range(1, len(xs)):
        d[i] = coeffs[i]
    for i in range(len(d)):
        d[i] = d[i] * (xs[i] - xs[i - 1])
    return d
