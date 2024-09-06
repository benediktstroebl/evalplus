def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.
    Args:
    xs (list): coefficients of the polynomial in order of increasing power, ex. [3, 1, 2, 4, 5] -> 3 + x^1 * 1 + x^2 * 2 + x^3 * 4 + x^4 * 5
    Returns:
    list: coefficients of the derivative represented in the same format as the input ex. [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + 1
    return result