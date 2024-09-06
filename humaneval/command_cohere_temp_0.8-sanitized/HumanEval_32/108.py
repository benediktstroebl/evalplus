import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Only returns the first solution, even if there are multiple zeros.
    Additionally, function works only for lists coefficients having an even number of coefficients
    and the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list must have an even length and a non-zero leading coefficient."

    # rearrange coefficients in descending order
    coefficients.sort(key = lambda x: -x)
    x = -coefficients[0] / (coefficients[1:] + [0.0])
    return x