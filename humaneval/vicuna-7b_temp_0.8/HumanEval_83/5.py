
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    count = 0
    for i in range(n):
        if i % 2 == 0:
            count += 1
    for i in reversed(range(n)):
        if i % 2 == 0:
            count += 1
    return count
