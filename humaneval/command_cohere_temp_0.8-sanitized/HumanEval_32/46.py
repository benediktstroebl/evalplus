import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, even if there are multiple.

    Preconditions:
        - coefficients must be an even number of coefficients and the greatest non-zero coefficient must be positive.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] < 0:
        raise ValueError("Must provide an even number of coefficients with the greatest non-zero coefficient positive.")

    # Divide coefficients into pairs.
    # Then we transform the problem solving -f(x) = 0 to finding y such that y^2 = f(x).
    # Finally we apply the quadratic formula to y to find x,
    # Taking the positive root in the case of ambiguity.
    pairs = zip(coefficients[1:], coefficients[2:])
    squared = [poly(pair, x) for pair, x in pairs]
    y = poly(squared, x)
    return -math.sqrt(y) if y else float('inf')