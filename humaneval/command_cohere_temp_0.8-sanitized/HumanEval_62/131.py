def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power of x.

    Returns:
        list: Derivative of the polynomial, represented as a list of coefficients.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    derivative_coef = 1
    for coef in xs:
        result[len(xs) - 1] += coef * derivative_coef
        derivative_coef += 1
    return result