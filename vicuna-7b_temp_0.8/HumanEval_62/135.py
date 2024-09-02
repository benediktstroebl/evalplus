

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) < 2:
        return [0]

    def derivative_helper(i, xs):
        if i == 0:
            return [0]
        else:
            return [xs[i-1], xs[i]-xs[i-1]]

    return [ derivative_helper(j, xs) for j in range(1, len(xs)+1) ]
