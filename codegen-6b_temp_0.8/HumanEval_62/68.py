

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    assert len(xs) >= 1
    for i in range(1, len(xs)):
        assert xs[i - 1] < 0 or xs[i - 1] >= 0
    ys = [1 if i == 0 else 0 for i, _ in enumerate(xs)]
    for i in range(len(xs) - 1):
        ys[i + 1] += xs[i] * i
    return ys
