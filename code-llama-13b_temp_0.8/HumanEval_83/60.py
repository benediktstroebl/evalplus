
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    one_ends = 10 ** (n-1) * 2
    starts_one = 10 ** (n-1) - 10 ** (n-2)
    return one_ends + starts_one
