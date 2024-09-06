import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the principle of completion.
    Requires that the list of coefficients have an even number of items, and the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return "Invalid input for coefficients list"
    
    # Scale coefficients by a power of 2 to maximize spread
    scale = 2**(len(coefficients) - 2)
    zeros = [poly(coefficients, x) for x in range(scale)]
    
    # Find the interval with a non-zero polynomial value
    interval_left, interval_right = -scale, scale
    while zeros[interval_left] == 0 and zeros[interval_right] == 0:
        if zeros[interval_left] < 0:
            interval_left += 1
        elif zeros[interval_right] < 0:
            interval_right -= 1
        else:
            return "Failed to find solution, possibly an invalid coefficient list"
    
    # Dichotomy until we find a zero
    left, right = interval_left, interval_right
    while left != right:
        mid = (left + right) // 2
        if zeros[mid] < 0:
            left = mid
        else:
            right = mid
    return left