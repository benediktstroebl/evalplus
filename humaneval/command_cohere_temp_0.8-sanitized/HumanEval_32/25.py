import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients, with the largest coefficient non-zero.
    """
    # Check that list has even length and largest coeff is not zero
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        raise ValueError("find_zero works with polynomials with even number of coefficients and largest coefficient non-zero")

    # Prepare coefficients in reversed order
    xs = [float(coeff) for coeff in coefficients[::-1]]

    # Binary search
    left, right = -1, 1
    while left + 1 < right:
        mid = (left + right) // 2
        if poly(xs, mid) == 0:
            return mid
        elif poly(xs, mid) > 0:
            left = mid
        else:
            right = mid
    else:
        return right