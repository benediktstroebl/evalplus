
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Handle the base case when n is 1
    if n == 1:
        return 1
    
    # If n is greater than 1, we need to handle the two cases separately
    count = 0
    for i in range(1, n):
        count += (10 ** (n - i - 1))
        
    count += (10 ** (n - 1))
    
    return count
