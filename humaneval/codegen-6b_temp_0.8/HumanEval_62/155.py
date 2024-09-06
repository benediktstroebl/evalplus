

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def derivative_helper(xs):
        if len(xs) == 0:
            return [0]
        elif len(xs) == 1:
            return [xs[0]]
        elif len(xs) == 2:
            return [xs[1]]
        else:
            return [xs[1]] + [x * n for x, n in zip(xs[2:], xs[1:])] + derivative_helper(xs[:-2])
    return derivative_helper(xs)

