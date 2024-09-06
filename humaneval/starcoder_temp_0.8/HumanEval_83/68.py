
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base Case: n is too small.
    if n < 10:
        return 1

    # Recursive Case: n is large enough.
    # 1. Count all starting with 1 and ending with a non-1 digit
    # 2. Count all starting with a non-1 digit and ending with 1
    # 3. Count all starting with a non-1 digit and ending with a non-1 digit
    return starts_one_ends(n-1) + starts_one_ends(n-1) + 1

