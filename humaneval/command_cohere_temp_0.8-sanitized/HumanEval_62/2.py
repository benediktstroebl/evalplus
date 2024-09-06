def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0]*(len(xs)-1)
    result[-1] = 1
    for i in range(len(xs)-2, -1, -1):
        result[i] = result[i+1] * len(xs) - result[i+1] * xs[i]
    return result