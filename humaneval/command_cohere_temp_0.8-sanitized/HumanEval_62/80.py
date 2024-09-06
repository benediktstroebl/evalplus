def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1j if i < n - 1 else 1    # imaginary number if not last iteration
        xs[i+1] *= 1j if i < n - 1 else 1  # imaginary number if not last iteration
    return result