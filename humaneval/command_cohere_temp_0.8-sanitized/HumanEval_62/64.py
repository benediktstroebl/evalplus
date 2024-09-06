def derivative(xs: list) -> list:
    """
    Return the derivative of the polynomial represented by the given list of coefficients.
    """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1
    return result