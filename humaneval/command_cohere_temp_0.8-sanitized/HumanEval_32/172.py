import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, based on the coefficients.
    Only returns one solution, and works only with lists of even numbers of coefficients.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    max_coefficient = max(coefficients)
    if max_coefficient == 0:
        raise ValueError("List of coefficients must have at least one non-zero element")

    # Solution based on factorization
    x = -max_coefficient / (sum(math.pow(i, max_coefficient) for i in range(1, len(coefficients) // 2 + 1)))
    return x