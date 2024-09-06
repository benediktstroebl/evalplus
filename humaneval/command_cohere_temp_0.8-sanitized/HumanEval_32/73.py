import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation: poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only with lists of even numbers of coefficients, and coefficients lists should be arranged so as largest absolute coefficient is first.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients list must have even number of coefficients')
    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError('largest coefficient must be non zero')
    # solution of quadratic equation - dx^2 + x - offset = 0
    d = [max_coeff, -coefficients[0] / max_coeff]
    x0, x1 = math.roots([d[0], d[1], -1])
    if x0 == x1:
        return x0
    else:
        raise ValueError('More than one root ('+str(x0)+', '+str(x1)+'). This should not happen.')