def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial expressed as a list of coefficients.

    Args:
        xs (list): Coefficients of the polynomial in the form [x^0, x^1, x^2, ...].

    Returns:
        list: Derivative of the polynomial in the same form.
    """
    result = [0] * len(xs)
    current_power = 1
    for x in xs:
        result[current_power - 1] += x * current_power
        current_power += 1
    return result