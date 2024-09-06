import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple solutions exist.
    
    Solution is found using regula falsi method, which is a root finding algorithm
    for polynomials with integer coefficients.
    
    regula falsi method has following properties:
    - Is capable of handling some cases where derivatives are awkward to calculate directly.
    - Is less susceptible to numeric instability relative to Newton's method.
    - Guarantees a solution, provided that max(coefficients) != 0.
    
    Precondition: len(coefficients) is even, and coeff[max_index] != 0
    where max_index is index of maximum coefficient.
    """
    max_index = len(coefficients) - 1
    max_coefficient = coefficients[max_index]
    assert len(coefficients) % 2 == 0
    assert max_coefficient != 0
    
    tol = max_coefficient / 1000
    x_prev, x_curr, x_next = -max_coefficient, -max_coefficient, 0
    
    while abs(x_curr - x_prev) > tol:
        x_prev, x_curr, x_next = x_curr, x_next, (x_curr + x_prev) / 2
        
        if abs(x_next) < tol and abs(poly(coefficients, x_next)) < tol:
            return x_next
    
    return x_curr