import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution x, if multiple solutions exist.
    Only operates on lists of coefficients with an even number of items
    and the list must must have the largest non-zero coefficient first, as this
    guarantees a solution.
    """
    # Your code here, remove this comment with your code

    # Poly should be 0 at x = -frac offending_coefficient to x
    # See https://www.geeksforgeeks.org/algorithmic-trick-to-find-all-zeroes-of-a-polynomial/
    return -coefficients[0] / (coefficients[1:] + [0])[0]