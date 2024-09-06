def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    n = len(xs) - 1
    derivative_coef = [0] * n
    x = 1
    for i in range(n):
        derivative_coef[i] = xs[i+1] * x
        x *= x
    return derivative_coef