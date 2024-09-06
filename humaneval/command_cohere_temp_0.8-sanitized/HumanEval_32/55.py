import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Only returns the first solution, even if there are multiple zeros.
    Guarantees a solution only for lists of coefficients with an even count
    and the largest coefficient not equal to zero.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Calculates discriminant of corresponding quadratic equation
    discriminant = (sum(coefficients[1:]) * len(coefficients) + sum(coefficients[1:])**2 / 4) / (len(coefficients) - 2)

    # Returns solution of quadratic equation for x
    return (-discriminant + math.sqrt(discriminant**2 - 4 * sum(coefficients[1:]) / (len(coefficients) - 2))) / 2