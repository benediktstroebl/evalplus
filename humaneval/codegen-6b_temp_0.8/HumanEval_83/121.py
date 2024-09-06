
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    
    from math import ceil, log10
    
    if n == 1:
        return 0
    
    return sum(int(ceil(log10(n) - log10(k) + 1)) for k in range(n, 0, -1))

