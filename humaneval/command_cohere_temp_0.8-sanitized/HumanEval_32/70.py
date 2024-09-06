import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, which is defined by the equation:
    sum(coeff * x**i for i, coeff in enumerate(coefficients))
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution x, if multiple solutions exist.
    
    Requires that the list coefficients have an even number of coefficients, 
    and that the largest non-zero coefficient be positive. This guarantees 
    that the leading coefficient of the polynomial is 1, and hence that 
    the polynomial has a single root.
    """
    # Make sure that the list has an even number of elements
    if len(coefficients) % 2 == 1:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    # Make sure that the largest non-zero coefficient is positive
    if coefficients[-1] < 0:
        raise ValueError("The largest non-zero coefficient must be positive.")
    
    # Let x = y - leading_coefficient / leading_coefficient
    # Then polynomial evaluates to 0 when y = leading_coefficient
    # So substitute that in:
    #   poly(y - leading_coefficient) = 0
    #   (y - leading_coefficient) * polynomial(leading_coefficient) = 0
    #   y - leading_coefficient = -leading_coefficient * polynomial(leading_coefficient) / polynomial_coefficient
    #   y = leading_coefficient + leading_coefficient * polynomial(leading_coefficient) / polynomial_coefficient
    #   y = (1 + polynomial_coefficient) * leading_coefficient
    # So x = (1 + polynomial_coefficient) * leading_coefficient
    return coefficients[0] + coefficients[0] * poly(coefficients[0]) / coefficients[1]