def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.
    Args:
    xs (list): Coefficients of the polynomial in the form [3, 1, 2, 4, 5].
    Returns:
    list: Derivative of the polynomial in the same form [1, 4, 12, 20].
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        if i != 0:
            result[i] //= i
    return result