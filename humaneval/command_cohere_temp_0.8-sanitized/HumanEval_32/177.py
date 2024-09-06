import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and the list must have the largest non-zero coefficient first.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('List of coefficients must have even length')
    max_idx = coefficients.index(max(coefficients))
    if len(coefficients) == 2:
        return -coefficients[1] / coefficients[0]
    else:
        x = -coefficients[max_idx] / coefficients[max_idx - 1]
        return poly_approx(x, coefficients, max_idx - 1)
def poly_approx(x: float, coefficients: list, degree: int) -> float:
    """Tries to find a better approximation of the zero of the polynomial."""
    approx_difference = abs(poly(coefficients, x))
    for i in range(degree + 1):
        x_new = x - approx_difference / coefficients[i]
        if abs(poly(coefficients, x_new)) < 1e-6:
            return x_new
    else:
        return x