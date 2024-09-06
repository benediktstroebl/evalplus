import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution, even if there are multiple zeros.
    Works only for lists with an even number of coefficients,
    and with the maximum absolute value non-zero coefficient.
    """
    # your code here, basically solve the equation by adapting an analytical method chosen
    # probably not the worst idea to start with bisection method
    if len(coefficients) % 2 == 1 or max(abs(coefficient) for coefficient in coefficients if coefficient) == 0:
        return "The input list of coefficients is not suitable for finding a solution"
    elif len(coefficients) == 2:
        return -coefficients[0] / (2 * coefficients[1])
    else:
        small = 1e-6
        big = 1e6
        x_mid = (small + big) / 2
        # we assume that the solution is somewhere in this interval
        for _ in range(205):  # Number of iterations chosen arbitrarily
            # but it better be enough...
            if poly(coefficients, x_mid) == 0:
                return x_mid
            elif poly(coefficients, x_mid) > 0:
                small = x_mid
            else:
                big = x_mid
            x_mid = (small + big) / 2
        return "Solution not found"