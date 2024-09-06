

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert isinstance(xs, list)
    assert len(xs) > 1
    assert all(isinstance(i, float) for i in xs)
    assert all(i >= 0 for i in xs)
    n = len(xs)
    result = [0] * (n - 1)
    for i in range(1, n):
        result[n - i - 2] = i * xs[n - i - 1]
    return result

