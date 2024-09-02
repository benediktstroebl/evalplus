

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def prod_list(lst, n=0):
        if n == len(lst):
            return [1]
        return [x * y for x, y in zip(lst, prod_list(lst, n + 1))]

    def deriv_list(lst, n=0):
        if n == len(lst):
            return []
        return [lst[n] * n + deriv_list(lst, n + 1)]

    return [x * n for x, n in zip(xs, prod_list(xs))] + \
        deriv_list(xs, 1)

