

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def helper(i, v):
        if i == len(xs):
            return [0]
        return [v[0] + v[1] * i, helper(i+1, v[1:])]

    return helper(1, xs)

