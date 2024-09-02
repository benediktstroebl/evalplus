
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    if n == 1:
        return 1
    if n == 2:
        return 1 + 1 + 1 + 1 + 1
    
    res = 0
    
    for i in range(1, 10):
        res += 9 * starts_one_ends(n-1)
        
    return res
