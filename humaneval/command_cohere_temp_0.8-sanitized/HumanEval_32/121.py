import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Uses the quadratic formula to find a solution, assuming the polynomial is quadratic.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        
    Returns:
        float: A solution x for the equation poly(x) = 0.
    Returns only one solution, even if there are multiple.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List coefficients must have an even number of elements.")
    if coefficients[-1] == 0:
        raise ValueError("Last coefficient must be non-zero.")
        
    # Ensuring coefficients are ordered to have the largest coefficient at index 0
    sorted_coefficients = sorted(coefficients)
    
    # Constructs quadratic equation ax^2 + bx + c = 0
    a = sorted_coefficients[-1]
    b = -sorted_coefficients[-2]
    c = 1
    
    # Using quadratic formula to find solution
    # Solution is always positive, so taking the positive one
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    return root1