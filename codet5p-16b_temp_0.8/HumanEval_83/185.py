
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    digits = [str(i) for i in range(10)]
    return starts_one_ends_helper(digits, n)
    
