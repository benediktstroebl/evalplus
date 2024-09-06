import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i equal to 0...n
    where n is len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple zeros exist.
    
    Solution is found using the following steps:
    1. Calculates corresponding polynomial from coefficients list.
    2. Checks if the polynomial has a zero solution using poly(x) = 0.
    3. If poly(x) = 0 has a solution, returns it.
    4. Otherwise returns first value of x where polynomial value is equal to 0.
    """ 
    polynomial = poly(coefficients, x)
    if polynomial == 0:
        return 0
    
    # grab the largest coefficient (will be the highest power of x)
    largest_coefficient = max(coefficients)
    
    # if the largest coefficient is 0, return 0
    if largest_coefficient == 0:
        return 0
    
    # Otherwise, create a list of zeros with an extra element at the end for x = 0.
    # This is to handle the edge case where the polynomial is always negative.
    # We also ensure that if the leading coefficient is positive, 
    # we flip the sign of the polynomial at the end
    x_values = [0]
    sign = 1 if largest_coefficient > 0 else -1
    while polynomial < 0:
        x_values.append(x_values[-1] + sign)
        polynomial += sign * poly(coefficients, x_values[-1])
        
    # Return the first zero point found
    return x_values[0]