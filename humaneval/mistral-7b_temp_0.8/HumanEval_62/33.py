

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def _derivative_core(xs: list, n):
        if n == 0:
            return 0
        else:
            return xs[n] + _derivative_core(xs, n-1) * (n-1)

    return [_derivative_core(xs, n) for n in range(len(xs))]

