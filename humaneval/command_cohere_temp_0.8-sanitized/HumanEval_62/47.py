def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial given its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs)):
        result[i] = xs[i] + x * result[i]
        x += 1
    return result