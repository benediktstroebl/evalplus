def derivative(xs: list) -> list:
    """
    Returns the derivative of a polynomial represented by its coefficients.
    xs[0] + xs[1]x + xs[2]x^2 + ...
    """
    n = len(xs) - 1
    derivative_coef = [0] * n
    for i in range(n):
        derivative_coef[i] = xs[i + 1] * (i + 1)
    return derivative_coef