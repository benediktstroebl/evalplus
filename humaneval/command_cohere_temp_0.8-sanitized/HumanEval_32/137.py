import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero parameter, in case there are more than one.
    Works only for lists with even number of coefficients, and assumes the greatest coefficient is not zero.
    """
    n = len(coefficients)
    # check n is even
    if n % 2:
        raise ValueError('find_zero works only for polynomials with even number of coefficients')
    # sort coefficients descending
    coefficients.sort(reverse=True)
    x = -coefficients[0] / (n // 2)
    for i in range(1, n // 2):
        x = x - coefficients[i] / (n // 2 - i)
    return x