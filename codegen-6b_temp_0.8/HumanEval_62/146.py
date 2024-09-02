

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
    assert all(isinstance(x, (int, float)) for x in xs)
    if len(xs) == 0:
        raise ValueError("No input")

    y = [1]
    for i in range(1, len(xs) + 1):
        y.append(xs[i - 1] * i)
    return y

