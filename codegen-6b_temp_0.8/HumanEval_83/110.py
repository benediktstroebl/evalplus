
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    i = 1
    while i <= n:
        if starts_one(i) or ends_one(i):
            count += 1
        i += 1
    return count

