import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that f(x) = 0.
    Returns only one solution, even in the case of multiple zeros.
    Works only for lists of coefficients with even length, and
    with the largest non-zero coefficient at the end (for efficiency in division).
    """
    n = len(coefficients)
    if n % 2 == 1 or coefficients[0] == 0:
        raise ValueError("find_zero works for lists of coefficients with even length, "
                         "and with the largest non-zero coefficient at the end.") 
    x = 0
    div = 10**10
    while div > 1:
        temp = coefficients[0] / div
        temp_poly = [temp]
        for i in range(1, n // 2):
            temp_poly.append(coefficients[i] / div)
        temp_poly.extend([temp] * (n // 2))
        if poly(temp_poly, x) == 0:
            return x
        div //= 10
    return None