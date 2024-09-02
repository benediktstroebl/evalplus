

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def _derivative(xs: list):
        if len(xs) <= 1:
            return [0]

        return [xs[0]] + [xs[i] * j for i in range(1, len(xs)) for j in [i, -1]]

    if not xs:
        raise ValueError('x vector must not be empty')

    return _derivative(xs)

