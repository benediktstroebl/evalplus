import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only for lists of coefficients with even length and largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return "Invalid input for find_zero()"
    # We solve x^2 * polynomial = 0, which has quadratic equation throot
    # Solution of that has a form: x = (-b (b2 - 4 ac) ) / (2 a)
    # So we create polynomial x^2 - b*x + (b2 - 4*max(coefficients)*max(coefficients))
    b = -max(coefficients)
    b2 = max(coefficients)**2 - 4 * max(coefficients) * min(coefficients)
    assert b2 > 0, "Must have largest non zero coefficient >= 2*smallest coefficient"
    a = 2 * max(coefficients)
    return (-b + math.sqrt(b2)) / a