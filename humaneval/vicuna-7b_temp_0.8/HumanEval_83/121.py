
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    count = 0
    for x in range(n):
        if x == 1:
            count += 1
        elif x % 10 == 1:
            count += 1
    return count
