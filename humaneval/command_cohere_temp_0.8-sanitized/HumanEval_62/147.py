def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
    return result