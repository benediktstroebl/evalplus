def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    xs_sorted = sorted(xs)
    n = len(xs_sorted) - 1
    derivative_coef = [0] * n
    for i in range(n):
        derivative_coef[i] = xs_sorted[i + 1] * (i + 1)
    return derivative_coef