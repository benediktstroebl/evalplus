

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def derivative_term(k: int, xs: list):
        """ Return coefficient of x^(k-1) in the derivative of p.
        >>> derivative_term(3, [1, 2, 3])
        6
        """
        if k == 1:
            return xs[0]
        if k > 1:
            return k * xs[k - 1]
        return 0
    return list(map(lambda x: derivative_term(x, xs), range(1, len(xs))))

