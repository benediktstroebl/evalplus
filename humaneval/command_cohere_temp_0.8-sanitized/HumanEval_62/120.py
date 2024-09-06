def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power.

    Returns:
        list: Derivative of the polynomial, again represented as a list of coefficients.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result