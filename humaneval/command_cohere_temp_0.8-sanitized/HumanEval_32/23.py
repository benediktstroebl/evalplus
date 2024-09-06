import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms where each term is a product of coefficient and x raised to the power of its index in the list.
    i.e. coefficients[0] * x^0 + coefficients[1] * x^1 + ... + coefficients[n] * x^n

    Args:
        coefficients (list): List of coefficients of the polynomial.
        x (float): Evaluates polynomial at this point.

    Returns:
        float: Evaluated polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial polynomial with coefficients coefficients such that poly(x) = 0.

    Args:
        coefficients (list): List of coefficients for the polynomial.

    Returns:
        float: A solution x for the polynomial equation poly(x) = 0.
    """
    # Check if list has an even number of coefficients and if it does, populate positives and negatives
    if len(coefficients) % 2 == 0:
        positives = [coeff for coeff in coefficients if coeff > 0]
        negatives = [coeff for coeff in coefficients if coeff < 0]
        if len(negatives) == 0:
            return find_zero_positive(positives)
        elif len(positives) == 0:
            return find_zero_negative(negatives)
        else:
            return find_zero_both(positives, negatives)
    else:
        raise ValueError("find_zero works for polynomials with an even number of coefficients")
def find_zero_positive(coefficients: list) -> float:
    """
    Helper function to find zero of polynomial with only positive coefficients.
    Starts from small x and moves till big x hoping to intersect curve.

    Args:
        coefficients (list): List of positive coefficients of the polynomial.

    Returns:
        float: A solution x for the polynomial equation poly(x) = 0.
    """
    # Start from a small value and go to a large value
    start = 1
    end = 10
    for i in range(start, end + 1):
        if poly(coefficients, i) == 0:
            return i
    return None
def find_zero_negative(coefficients: list) -> float:
    """
    Helper function to find zero of polynomial with only negative coefficients.
    Starts from big x (will never intersect) and comes down till small x (may or may not intersect).
    If we intersect, return that x, else return None.

    Args:
        coefficients (list): List of negative coefficients of the polynomial.

    Returns:
        float: A solution x for the polynomial equation poly(x) = 0.
    """
    # Start from a large value and go to a small value
    start = 10
    end = 1
    for i in range(start, end - 1, -1):
        if poly(coefficients, i) == 0:
            return i
    return None