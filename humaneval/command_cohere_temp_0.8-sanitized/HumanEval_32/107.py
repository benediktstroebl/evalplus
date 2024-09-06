import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero, i.e. there may be more than one.
    Works only for lists with even number of coefficients, and maximal coefficient != 0
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('list of coefficients must have even number of elements')
    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError('max coefficient must be != 0')

    # solve quadratic equation with constants sum -a*d
    a = -coefficients[-1] / max_coeff
    d = 4 * a
    sum_ = coefficients[0] / max_coeff
    x = sum_/(d - math.sqrt(d**2 - sum_*sum_))
    return x