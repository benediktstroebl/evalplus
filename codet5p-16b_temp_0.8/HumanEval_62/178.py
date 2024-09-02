

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    derivative_coefficients = []
    n = len(xs)
    for i in range(n):
        if i == n - 1:
            derivative_coefficients.append(n * xs[i])
        else:
            derivative_coefficients.append(xs[i + 1] * (n - i - 1))
    return derivative_coefficients

