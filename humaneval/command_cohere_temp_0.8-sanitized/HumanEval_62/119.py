def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs where xs[i] is the coefficient of x^i.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    ys = [0] * (len(xs) + 1)
    ys[0] = 1
    for x, y in zip(xs, ys):
        ys = [y + x * x * ys[i+1] / (i + 1) for i, y in enumerate(ys)]
    return ys[:-1]