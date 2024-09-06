def derivative(xs: list) -> list:
    """
    Return the derivative of the polynomial represented by the list of coefficients.
    """
    result = [0] * (len(xs) + 1)
    result[0] = 1
    for i in range(len(xs)):
        result[i+1] = result[i] * len(xs) - xs[i] * result[i]
    return result