def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial given its coefficients.

    Args:
        xs (list): The coefficients of the polynomial, in the order:
                    xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns:
        list: The coefficients of the derivative, in the same format as the input.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result