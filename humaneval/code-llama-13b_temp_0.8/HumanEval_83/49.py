
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Counting all n-digit numbers
    count = 10**(n-1)
    
    # Counting all n-digit numbers that start with 1
    count += 10**(n-2)
    
    # Counting all n-digit numbers that end with 1
    count += 10**(n-2)
    
    # Returning result
    return count
