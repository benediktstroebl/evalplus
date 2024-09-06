import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero solution, even if there are more.
    Works only for lists coefficients having an even number of coefficients
    and the largest non-zero coefficient, as it guarantees
    a solution.
    """
    n = len(coefficients)

    # Check for valid input
    if n % 2 == 1 or coefficients[n // 2] == 0:
        raise ValueError("Input coefficients list must have an even length"
                         " and contain a non-zero coefficient")

    # Calculate the zero boundary
    zero_boundary = [-coefficients[n // 2] / (n // 2 + 1)]

    # Iteratively find the zero solution using binary search
    for i in range(n // 2):
        # Calculate the boundary for this iteration
        boundary = [zero_boundary[0] - coefficients[i] / (i + 2)]
        # Binary search between boundaries
        x = bisect(boundary, 0)
        zero_boundary = [x] * 2

    return zero_boundary[0]
def bisect(a, x):
    """
    Returns index of x in a if x is in a, or nearest index to x if x is not in a.
    """
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo