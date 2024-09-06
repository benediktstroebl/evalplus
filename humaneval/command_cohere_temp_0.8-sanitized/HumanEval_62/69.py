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
    for i in range(len(xs)):
        for j in range(len(ys)):
            if j + 1 < len(ys):
                ys[j + 1] += xs[i] * ys[j]
        ys[i + 1] += xs[i] * i
    return ys[:-1]