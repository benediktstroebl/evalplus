import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Works only for polynomials with even number of coefficients
    and largest non-zero coefficient, as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 0: 
        max_coeff = max(coefficients)
        if max_coeff != 0:
            return (max_coeff) ** (1/2)
    else:
        print('Coefficients list must have even number of elements')
    return None