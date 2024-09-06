import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient, as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("List coefficients should have even length and largest non-zero coefficient.")

    x = -coefficients[0] / coefficients[-1]
    temp = [x]
    for i in range(1, len(coefficients) // 2 + 1):
        x = x - coefficients[i] / coefficients[-(i + 1)]
        temp.append(x)
    
    # so that solution is within [0, 1]
    return min(temp)