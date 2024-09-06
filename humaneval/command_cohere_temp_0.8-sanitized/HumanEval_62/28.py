def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.

    Args:
        xs (list): Coefficients of the polynomial in the form [3, 1, 2, 4, 5], where xs[0] is the constant term and xs[1:] are the terms with multiplying factors x, x^2, ..., x^n.

    Returns:
        list: The derivative of the polynomial in the same form.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + 1
    return result