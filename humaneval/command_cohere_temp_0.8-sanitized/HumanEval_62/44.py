def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    result = [0]*len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i]*x
        x *= 1
    return result