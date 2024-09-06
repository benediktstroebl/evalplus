def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    num_terms = len(xs) - 1
    derivative_coef = [0] * num_terms
    x = 1
    for i in range(num_terms):
        derivative_coef[i] = xs[i+1] * x
        x *= 2
    return derivative_coef