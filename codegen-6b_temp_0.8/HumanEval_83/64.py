
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 9
    elif n == 2:
        return 10
    count = 0
    for i in range(1, 9):
        if i <= n:
            count += 10**i
    return count

