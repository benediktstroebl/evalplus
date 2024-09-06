import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x such that poly(x) = 0 for the given polynomial coefficients.
    Guarantees to find only one solution, even if there are multiple zeros.
    Requires that the list coefficients have an even number of elements
    and the largest non-zero coefficient to have a guaranteed solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        raise ValueError("List of coefficients must have an even number of elements and a non-zero largest coefficient.")
    x = 0
    max_coeff = max(coefficients)
    while max_coeff > 0:
        x += 1
        power_x = len(coefficients) - 1
        # invariant: max_coeff == max_coeff * (1 + x^2)^power_x
        # when max_coeff is negative, it's a quadratic with an obviously negative coefficient,
        # so the value of the polynomial is negative (and therefore has no real solutions)
        while max_coeff < 0:
            power_x -= 1
            max_coeff *= (1 + x*x)**power_x   # <- this is the key transformation
        # when max_coeff is 0, polynomial value is 0
        # solution is x satisfying: power_x == 0
        # => x = sqrt(-power_x / (2 * max_coeff))
        x = math.sqrt(-power_x / (2 * max_coeff))
    return x