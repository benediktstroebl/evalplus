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
    Finds a solution x for the polynomial equation coefficients[i] * x**i = 0.
    Returns only the first found zero solution, if multiple zeros exist.
    Guarantees a solution if coefficients have an even number of elements
    and the largest non-zero coefficient is positive.
    """
    # Ensure valid input
    if len(coefficients) % 2 == 1 or max(coefficients) < 0:
        raise ValueError("Input coefficients list must have an even number of elements and positive max value")
    
    # Initials solutions vector to span all possible solutions
    solutions = [x / coefficients[0] for x in range(len(coefficients))]
    
    # Find zero solution using bisection method
    while len(solutions) > 1:
        mid = (solutions[0] + solutions[-1]) / 2
        if poly(mid, mid) == 0:
            solutions = [mid] + solutions[1:]
        else:
            solutions = solutions[:-1]
    return solutions[0]