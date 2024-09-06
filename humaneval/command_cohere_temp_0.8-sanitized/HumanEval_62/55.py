def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed in sums of powers of x.
    Args:
        xs (list): Coefficients of the polynomial, in order of ascending power of x.
    Returns:
        list: Derivative of the polynomial, in the same format.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        x -= xs[i] / (i + 1)
    return result