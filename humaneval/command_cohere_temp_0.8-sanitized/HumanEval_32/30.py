import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only one solution, even if there are many.
    Also, it only accepts lists of coefficients that have an even length
    and the greatest magnitude coefficient, as this guarantees a solution.
   Returns the solution x, which is calculated using the formula:
    x = -sum(coeff / (i * i) for i, coeff in enumerate(coefficients))
    """
    # Your code here, but make sure it works for even lengths and positive magnitudes
    if len(coefficients) % 2 == 1 or max(abs(coefficients), key=abs) == 0:
        return "Invalid input"
    x = -sum([coeff / (i * i) for i, coeff in enumerate(coefficients)])
    return x