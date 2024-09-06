
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    s = str(n)
    if s.startswith('1'):
        if s.endswith('1'):
            return n
        else:
            return n - 1
    elif s.endswith('1'):
        return n - 1
    else:
        return 0
