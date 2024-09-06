def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs """
    result = [0] * (len(xs) - 1)
    degree = len(xs) - 1
    for i in range(degree):
        result[i] = xs[i + 1] * (degree - i)
    return result