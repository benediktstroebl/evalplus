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
    derivative_sum = [0] * (len(xs) + 1)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs) + 1):
            derivative_sum[j] += xs[i] * j
    return derivative_sum[:-1]