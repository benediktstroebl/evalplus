
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for num in range(1, n+1):
        if str(num).startswith(str(1)):
            count += 1
    for num in reversed(range(n+1)):
        if str(num).endswith(str(1)):
            count += 1
    return count
