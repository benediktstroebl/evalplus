def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1
    return result