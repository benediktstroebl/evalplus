import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    n = len(coefficients)
    # check n is even
    if n % 2:
        print("Error: list of coefficients must have even length")
        return None
    # conjugate pairs of coefficients
    xs, ys = zip(*[complex(coef, 0) for coef in coefficients])
    # solve Ax = b using x = (A^-1)y
    x = sum(ys / (xs - ys))
    # solution
    return x