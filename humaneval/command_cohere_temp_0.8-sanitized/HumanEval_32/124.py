import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution, even if there are multiple zeros.
    Guarantees a solution only for lists of coefficients with an even count
    and the largest non-zero coefficient.
    """
    # Check if list has an even number of elements
    if len(coefficients) % 2 == 1:
        return "List of coefficients must have an even number of elements"
    
    # Find the largest non-zero coefficient
    max_coeff = max(coefficients, key=lambda x: abs(x))
    
    # Divide all coefficients by the largest coefficient
    coefficients = [num / abs(max_coeff) for num in coefficients]
    polynomial = poly(coefficients, x=0)
    
    # If polynomial is zero at 0, means max_coeff was a redundant factor
    if polynomial == 0:
        return 0
    
    # Find the root using the polynomial formula
    root = poly(coefficients, x=-1) / poly(coefficients, x=1)
    return root