def derivative(xs: list) -> list:
    """
    Return the derivative of the polynomial represented by the list of coefficients.
    """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (x + 1) - xs[i]
        x += 1
    return result