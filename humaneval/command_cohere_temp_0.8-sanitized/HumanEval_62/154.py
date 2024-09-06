def derivative(xs: list) -> list:
    """
    Return the derivative of a polynomial expressed as a list of coefficients.
    """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs)):
        result[i] = xs[i] / (i + 1)
        x += 1
        while x == i + 1:
            result[i] += xs[x] / (x + 1)
            x += 1
    return result