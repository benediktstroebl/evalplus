import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and assumes the largest coefficient is the constant term.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('Function works with lists of even number of coefficients.')
    max_coeff = max(coefficients)
    if not max_coeff:
        raise ValueError('Function assumes largest coefficient is the constant term.')
    
    # Divide polynomial with largest coefficient as constant
    # i.e x^n - (largest_coeff + small_coeffs) * x^(n-1)
    n = len(coefficients) - 1
    x_n_minus_1 = poly(coefficients[:-1], -1)
    solution = -max_coeff / x_n_minus_1
    return solution