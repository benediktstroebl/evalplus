import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients polynomial such that poly(x) = 0.
    Returns only one solution, even in the presence of multiple zeros.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient.
    """
    # make sure list has even number of coefficients and
    # contains a non-zero coefficient
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return "coefficients list must have even length, and contain a non-zero coefficient"
    # make sure the leading non-zero coefficient is twice the coefficient
    # that follows it
    if coefficients[-2] == 0:
        return "List must have a non-zero coefficient before the leading coefficient."
    leading_coef, next_coef = coefficients[-1], coefficients[-2]
    multiple = leading_coef / next_coef
    if not multiple.is_integer():
        return "Leading coefficient must be divisible by the second largest coefficient"
    return next_coef * multiple - leading_coef