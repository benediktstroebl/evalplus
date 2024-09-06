import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and coefficients lists with the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients list must have an even number of coefficients')
    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError('largest coefficient must be non zero')

    # solve quadratic equation ax^2 + ax = -max_coeff
    a = max_coeff
    x_sq = (-a + math.sqrt(a**2 - 4*a*max_coeff)) / (2*a)
    if x_sq < 0:
        return find_zero([-coefficients[0], -coefficients[1]])
    return x_sq