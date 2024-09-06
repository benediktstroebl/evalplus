import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.
        
    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution for the equation polynomial = 0.
    Returns the value of x at which the polynomial evaluates to zero.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        
    Returns:
        float: A floating-point number representing the value of x at which the polynomial equals zero.
    """
    # Check for an even number of coefficients and a non-zero coefficient
    if len(coefficients) % 2 == 0 and coefficients[-1] != 0:
        # Calculate the polynomial value for x = -coefficient
        x = -coefficients[-1]
        if poly(coefficients, x) == 0:
            return x
        
        # Start with a guess close to x = -coefficient and use binary search
        left, right = -coefficients[-1] - 1, -coefficients[-1] + 1
        while left <= right:
            mid = (left + right) / 2
            if poly(coefficients, mid) == 0:
                return mid
            elif poly(coefficients, mid) > 0:
                left = mid + 1
            else:
                right = mid - 1
    else:
        raise ValueError("Invalid input. The list of coefficients must have an even number of elements and a non-zero coefficient.")