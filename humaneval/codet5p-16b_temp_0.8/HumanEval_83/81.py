
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    total = 0
    for x in range(1, n):
        total += starts_one_ends_1_ends(x)
    return total
    
    
