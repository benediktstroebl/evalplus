import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation p(x) = 0.
    Only returns the first solution found, if multiple solutions exist.
    
    Requires the provided list of coefficients to have an even number of coefficients 
    and the largest non-zero coefficient for guarantee of a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Invalid input. Must provide an even number of coefficients and a largest non-zero coefficient."

    # oversize coefficients and subtract polynomial
    x = -coefficients[0] / coefficients[1]
    temp = [0] * ((len(coefficients) // 2) + 1)
    temp[0] = 1
    for i in range(1, len(temp)):
        temp[i] = temp[i - 1] * x
    temp_pol = poly(temp, x)

    # oversize coefficients and add polynomial
    x = coefficients[0] / coefficients[1]
    temp = [0] * ((len(coefficients) // 2) + 1)
    temp[0] = 1
    for i in range(1, len(temp)):
        temp[i] = temp[i - 1] * x
    temp_pol += poly(temp, x)

    # now temp_pol is oversised with offset
    for i in range(len(temp_pol)):
        if temp_pol[i] == 0:
            continue
        else:
            break
    else:
        return "No solution found"

    # binary search
    lo, hi = -10, 10
    while hi - lo > 1e-5:
        x_mid = (hi + lo) / 2
        if poly(temp, x_mid) > 0:
            hi = x_mid
        else:
            lo = x_mid
    return lo