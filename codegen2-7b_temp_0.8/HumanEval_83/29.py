
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    i = 1
    while i < n:
        if i.startswith('1'):
            return i
        else:
            i += 1
    return
