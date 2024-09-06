def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial expressed in list form.

    Args:
        xs (list): Coefficients of the polynomial, with earlier powers kept to the left.

    Returns:
        list: Coefficients of the derivative, with the same ordering as the input.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result