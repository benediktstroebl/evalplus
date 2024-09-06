import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple zeros exist.
    
    Guarantee: Requires list coefficients to have an even length, and the largest non-zero coefficient to be present.
    """
    assert len(coefficients) % 2 == 0, "Requires list coefficients to have even length."
    max_coeff = max(coefficients)
    assert max_coeff != 0, "Requires largest non-zero coefficient to be present."
    
    # Handle case of constant function
    if len(coefficients) == 2:
        return -1 / max_coeff
    
    # Split coefficients into pairs
    halves = [coefficients[i:i+2] for i in range(0, len(coefficients), 2)]
    
    # Try each pair of coefficients as roots
    for pair in halves:
        x = -poly(pair, x=1 / max_coeff)
        if x:
            return x
    
    # If no valid roots, return NaN as an indication of error
    return math.nan