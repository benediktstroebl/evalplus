def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    result = [0] * (len(xs) - 1)
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (i + 1)
    return result