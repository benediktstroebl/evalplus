def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    n = len(xs) - 1
    derivative_coefficients = [0] * n
    x = 1
    for i in range(n):
        xs_i = xs[i]
        derivative_coefficients[i] = xs_i * x
        x *= 1j
    return derivative_coefficients