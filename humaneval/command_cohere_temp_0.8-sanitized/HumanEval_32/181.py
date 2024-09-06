import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only one solution, even if there are many.
    Also, it assumes that the list coefficients has an even number of coefficients
    and the largest non-zero coefficient, as it guarantees
    a solution.
    """
    # Your code here. Make sure to implement these variables:
    n = len(coefficients)
    var = coefficients[n // 2]
    half = n // 2
    neg = [-coefficients[2 * i] / coefficients[half] for i in range(half)]
    sols = []
    for m in range(1, half):
        x = -neg[m - 1] / neg[m]
        sols.append(x)
    # Determine the solution based on the sign of the leading coefficient
    if var > 0: 
        return sols[0]
    elif var < 0: 
        return sols[1]
    else: 
        return None