def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial whos coefficients are represented by xs
    e.g.: xs[0] + xs[1] * x + xs[2] * x^2 + ... 
    """
    result = [0] * len(xs)
    result[0] = 1
    for i in range(1, len(xs)):
        result[i] = result[i - 1] * 1.0 + xs[i] * (i + 1)
    return result