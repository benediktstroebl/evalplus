

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    n = len(xs)
    derivative_value = 0
    for i in range(n):
        if i == 0:
            derivative_value = xs[1]
        else:
            derivative_value += (n - i) * xs[i]
    return derivative_
