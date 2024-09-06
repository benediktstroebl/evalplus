def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1 + i
    return result