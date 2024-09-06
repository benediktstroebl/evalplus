
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    
    total = 1
    for i in range(1, 11**(n-1)):
        total += (9 * 10**(n-1))

    return total

