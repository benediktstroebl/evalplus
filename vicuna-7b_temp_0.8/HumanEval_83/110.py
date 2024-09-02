
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 1
    # recursive case
    count = 0
    for i in range(n // 2, -1, -1):
        if n % i == 1:
            count += 1
    return count
