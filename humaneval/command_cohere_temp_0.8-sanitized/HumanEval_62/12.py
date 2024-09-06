def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs) - 1):
        result[i] = xs[i+1] * (1 if i == len(xs) - 2 else x)
        x += xs[i]
    return result