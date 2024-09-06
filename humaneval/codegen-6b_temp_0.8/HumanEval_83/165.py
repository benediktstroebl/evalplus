
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n = list(str(n))
    if len(n) == 1:
        return 0
    if n[0] == '1':
        return starts_one_ends(n[1:]) + 1
    if n[-1] == '1':
        return starts_one_ends(n[:-1]) + 1
    return starts_one_ends(n[1:]) + starts_one_ends(n[:-1])

