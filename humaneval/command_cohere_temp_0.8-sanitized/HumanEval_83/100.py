def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    
    # Calculate the total number of n-digit numbers.
    total = 10**n
    
    # Calculate the count of numbers that start with 1.