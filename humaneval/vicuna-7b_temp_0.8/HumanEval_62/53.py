

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
    result = [[0] * (length + 1) for _ in range(length)]
    result[0][0] = xs[0]
    for i in range(1, length + 1):
        for j in range(i - 1, -1, -1):
            result[i][j] = result[i - j][0]
    for i in range(2, length):
        result[i][i] = result[i - 1][0]
    return result
