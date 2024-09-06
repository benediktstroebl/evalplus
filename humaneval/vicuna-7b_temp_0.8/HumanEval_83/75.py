
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 1
    
    # loop case
    count = 0
    for i in range(n-1, 0, -1):
        # increment count if the number starts with 1
        if n % i == 0 and n % (i+1) != 0:
            count += 1
    
        # increment count if the number ends with 1
        if i < n-1 and n % i == 0:
            count += 1
    
    return count