def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    num_terms = len(xs) - 1
    result = [0] * num_terms
    x = 1
    for i in range(num_terms):
        result[i] = xs[i+1] * x
        x *= 2
    return result