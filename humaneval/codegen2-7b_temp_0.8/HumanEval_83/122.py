
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num = 0
    for i in range(10):
        num += starts_ends(i, n)
    
