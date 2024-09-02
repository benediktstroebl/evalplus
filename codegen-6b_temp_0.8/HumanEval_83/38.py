
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    d = str(n)
    if d[0] == '1':
        return n
    return starts_one_ends(n-1) + n

