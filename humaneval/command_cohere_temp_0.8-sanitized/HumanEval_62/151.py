def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial expressed in coefficients.
    Polynomial is represented as a list of coefficients for each power.
    i.e. [3, 1, 2, 4, 5] is interpreted as 3 + 1x + 2x^2 + 4x^3 + 5x^4.
    Returns: a list of coefficients of the derivative.
    """
    result = [0] * (len(xs) + 1)
    result[0] = 1
    for i in range(len(xs)):
        result[i+1] = result[i] * len(xs) - xs[i] * result[i]
    return result