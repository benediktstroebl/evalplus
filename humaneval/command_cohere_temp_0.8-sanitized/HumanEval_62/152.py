def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    derivative_coefficients = [0] * n
    for i in range(n):
        derivative_coefficients[i] = xs[i + 1] * (i + 1)
    return derivative_coefficients