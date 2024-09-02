
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # handle n=1, n=2 separately
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        # base case
        count = 1
        for i in range(1, n):
            count += starts_one_ends(n - i)
        return count
