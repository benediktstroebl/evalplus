import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero as this
    guarantees a solution.
    """
    # make list of coeffs positive and ordered
    coefficients = sorted(coefficients)[::-1]
    # Invert sign for even numbered coeffs
    coefficients[::2] = [-coeff for coeff in coefficients[::2]]
    # Result from polynomial equation is sum of terms with even i
    even_index_sum = sum(coefficients[i] * math.pow(i, i) for i in range(len(coefficients)))
    # Solve equivalence equation sum of terms with even i = 0
    return -math.sqrt(math.pow(even_index_sum, 2) / (4 * sum(coefficients[i] * math.pow(i, i-1) for i in range(len(coefficients)))))