import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients such that poly(x) = 0.
    Returns only the first found zero.
    Works only for lists of even numbers of coefficients, and assumes the greatest coefficient is the leading coefficient.
    """
    leading_coefficient = max(coefficients)
    half_order = len(coefficients) // 2
    if not len(coefficients) % 2 or not leading_coefficient:
        raise ValueError("List of coefficients must be of even length and leading coefficient must be greater than 0.") 
    if len(coefficients) == 2:
        return -leading_coefficient / (2 * leading_coefficient - coefficients[1])
    else:
        # solve quadratic equation with form x^2 + ... + leading_coefficient x 0
        root = (-leading_coefficient) / (2 * math.sqrt(leading_coefficient ** 2 + sum([coeff ** 2 for coeff in coefficients[1:-1]])))
        return root