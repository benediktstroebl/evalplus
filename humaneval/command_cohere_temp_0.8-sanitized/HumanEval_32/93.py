import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms where each term is coeff times (x^i)
    i starts from 0 and goes till len(xs)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Solution x is guaranteed to exist and is unique.
    Returns only one zero point, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes that the list contains the largest non-zero coefficient.
    """
    # Your code here, make sure to return a float
    if len(coefficients) % 2 == 1:
        raise ValueError('List of coefficients must have an even number of elements')
    max_coefficient = max(coefficients)
    if max_coefficient == 0:
        raise ValueError('List of coefficients must contain a non-zero coefficient')

    # Calculate the root x such that polynomial evaluates to zero
    x = -max_coefficient / (poly(coefficients, -max_coefficient) / max_coefficient)
    return x