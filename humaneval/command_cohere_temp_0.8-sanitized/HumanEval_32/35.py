import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Works only for lists with even number of coefficients,
    and where largest non-zero coefficient is present.
    Returns one solution x.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return None

    # flip sign to negative
    x = -coefficients[-1] / (2 * coefficients[-2])
    # equation should be sum of (x-1)(x-2)...(x-(n-1)) = 0
    for i in range(1, len(coefficients) // 2):
        x = x - coefficients[i] / (i + 1)

    return x