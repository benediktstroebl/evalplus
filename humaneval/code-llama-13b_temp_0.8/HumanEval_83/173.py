
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2

    count = 0

    # 1 followed by (n-1) 0's
    count += 10 ** (n-2)
    # 0 followed by (n-1) 1's
    count += 10 ** (n-2)

    return count
