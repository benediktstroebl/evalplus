

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    x = 0
    for i, _ in enumerate(xs):
        if x == 0:
            x = 1
        else:
            x = i
        y = 0
        for j, _ in enumerate(xs):
            if j == x:
                y = 1
            elif j == i:
                y = xs[j]
            else:
                y = 0
        xs[i] = y
    return xs
