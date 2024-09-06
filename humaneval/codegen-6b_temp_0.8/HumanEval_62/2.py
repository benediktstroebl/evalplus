

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    "*** YOUR CODE HERE ***"
    res = []
    while len(xs) > 1:
        new = xs[1]
        if len(xs) > 2:
            new += xs[2] * 2
        if len(xs) > 3:
            new += xs[3] * 3
        if len(xs) > 4:
            new += xs[4] * 4
        if len(xs) > 5:
            new += xs[5] * 5
        res.append(new)
        xs = xs[1:]
    return res

