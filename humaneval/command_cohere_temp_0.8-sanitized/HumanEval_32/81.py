import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only one zero point, even if there are many.
    Works only with lists coefficients having even number of coefficients
    and largest non zero coefficient, as it guarantees
    a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return "coefficients list must have even length and define highest coefficient to find a solution."
    elif len(coefficients) == 2:  # special case of linear function
        return -coefficients[0] / coefficients[1]
    else:
        # split coefficients into highest and rest
        highest = coefficients[-1]
        rest = coefficients[:-1]
        # repeatedly solve for rest*x + highest
        # until result is within interval [0, highest]
        while True:
            x = (-rest @ x) / highest
            if abs(x) <= 1:
                return x
            elif x > 1:
                rest = [-c for c in rest if c != 0] + [highest]
            else:
                rest = [-c for c in rest if c != 0] - [highest]