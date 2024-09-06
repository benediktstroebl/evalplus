import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, even if there are multiple.
    Works only for lists of coefficients with even length, and largest non-zero coefficient.
    """
    assert len(coefficients) % 2 == 0, "find_zero works only with even length lists of coefficients"
    max_coeff = max(coefficients)
    assert max_coeff != 0, "find_zero works only with lists with largest non-zero coefficient"

    # pick left or right half of divide and conquer, based on sign of max_coeff
    if max_coeff > 0:
        return find_zero_positive(coefficients, max_coeff)
    else:
        return find_zero_negative(coefficients, -max_coeff)
def find_zero_positive(coefficients, max_coeff):
    # iterate through even half of coefficients, trying to find zero
    for i in range(len(coefficients) // 2):
        x = (max_coeff - coefficients[i]) / (max_coeff + coefficients[i])
        if abs(x) < 1e-6:  # handle floating point precision issues
            return x
    # if no solution exists in even half, iterate through odd half
    for i in range(len(coefficients) // 2 - 1, -1, -1):
        x = (max_coeff - coefficients[i]) / (max_coeff + coefficients[i])
        if abs(x) < 1e-6:  # handle floating point precision issues
            return x
def find_zero_negative(coefficients, neg_max_coeff):
    # neg_max_coeff is the negative of the largest coefficient
    # iterate through odd half of coefficients, trying to find zero
    for i in range(len(coefficients) // 2 - 1, -1, -1):
        x = (neg_max_coeff - coefficients[i]) / (neg_max_coeff + coefficients[i])
        if abs(x) < 1e-6:  # handle floating point precision issues
            return x
    # if no solution exists in odd half, iterate through even half
    for i in range(len(coefficients) // 2):
        x = (neg_max_coeff - coefficients[i]) / (neg_max_coeff + coefficients[i])
        if abs(x) < 1e-6:  # handle floating point precision issues
            return x