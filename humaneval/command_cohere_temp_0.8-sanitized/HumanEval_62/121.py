def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    n = len(xs) - 1
    derivative_coef = [0] * n
    for i in range(n):
        derivative_coef[i] = xs[i + 1] * (i + 1)
    return derivative_coef