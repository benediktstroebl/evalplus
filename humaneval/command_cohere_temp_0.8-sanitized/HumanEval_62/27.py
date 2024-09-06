def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result