def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs where xs[i] is the coefficient of x^i. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * (i+1)
    return result