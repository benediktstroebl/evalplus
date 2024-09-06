

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if xs[0] == 0:
        return [0]
    i = 1
    derivative = []
    while i < len(xs) - 1:
        derivative.append((xs[i] * i))
        i = i + 1
    return derivative

