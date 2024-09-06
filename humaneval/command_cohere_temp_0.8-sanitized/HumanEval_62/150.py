def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs where xs[0] is the constant term and xs[1:] are the coefficients of the polynomial multiplied by x^0, x^1, x^2, ... respectively.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = [0] * (len(xs) - 1)
    result.append(1)
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * len(xs) - xs[i]
    return result