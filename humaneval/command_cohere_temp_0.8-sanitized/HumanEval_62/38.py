def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients in xs. """
    n = len(xs) - 1
    deriv = [0] * n
    x = 1
    for i in range(n):
        deriv[i] = xs[i+1] * x
        x *= 1j
    return deriv