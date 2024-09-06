

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    def f(x, a):
        return sum(a[i] * x ** i for i in range(len(a)))

    # return [0] + list(map(sum, zip(xs[1:], [0] + xs[:-1])))

    return [0] + [f(1, xs[1:])]


