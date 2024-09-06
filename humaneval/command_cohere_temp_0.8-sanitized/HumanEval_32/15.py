import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("List coefficients must have even length and largest non-zero coefficient")
        
    # Calculate polynomial value at x = 0
    initial_value = poly(coefficients, 0)
    
    # Prepare coefficients in format [coefficient_to_x^2, coefficient_to_x]
    even_coefficients = [coefficients[i] for i in range(0, len(coefficients), 2)]
    
    # Calculate polynomial value at x = 1
    intermediate_value = poly(even_coefficients, 1)
    
    # Calculate solution
    solution = -initial_value / intermediate_value
    return solution