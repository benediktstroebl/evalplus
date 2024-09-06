import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple solutions exist.

    Preconditions:
        - coefficients must be a list of even number of coefficients,
          with the largest non-zero coefficient first.
    """
    # check preconditions
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients must be of even length')
    max_idx = coefficients.index(max(coefficients))
    if max_idx != len(coefficients) // 2:
        raise ValueError(
            'largest non-zero coefficient must be first in the list')

    # solution algorithm
    x = -coefficients[0] / coefficients[1]
    y = (coefficients[len(coefficients) // 2] * x) / coefficients[len(coefficients) // 2 - 1]
    for i in range(len(coefficients) // 2 - 2, -1, -1):
        x -= (coefficients[i] / coefficients[i + 1]) * (y / coefficients[i])
    return x