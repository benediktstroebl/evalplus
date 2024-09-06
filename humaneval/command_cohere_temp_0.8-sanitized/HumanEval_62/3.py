def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs[0], xs[1]x, xs[2]x^2, etc. """
    result = [0]*len(xs)
    dx = 1
    for i in range(len(xs)):
        result[i] = xs[i]*dx
        dx *= 1
    return result