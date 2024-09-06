

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def _derivative(xs):
        if len(xs) == 1:
            return [0]
        elif len(xs) == 2:
            return [xs[1]]
        else:
            return [sum(xs[1:i+1]) for i in range(1, len(xs))]
    return reduce(_derivative, xs)
