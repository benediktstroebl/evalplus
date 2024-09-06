

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    length = len(xs)
    derivative = [0] * length
    for i in range(length):
        derivative[i] = xs[i]
        for j in range(i + 1, length):
            derivative[i] += xs[j] * (i - j + 1)
    return derivative
