

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    ys = [next(iter(zip(xs, [0] + [int(i) for i in str(x)])) for x in xs) for _ in range(1, len(xs) + 1)]
    return [int(i[0]) - i[1] * i[2] for i in ys]
