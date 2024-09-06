
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    s = str(n)
    if s[0] == '1' or s[-1] == '1':
        return 1
    else:
        return 0
