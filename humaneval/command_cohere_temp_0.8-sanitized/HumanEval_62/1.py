def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0]*(len(xs)-1)
    result[0] = 1
    for i in range(len(xs)-1):
        result[i+1] = result[i] + xs[i+1]
    return result