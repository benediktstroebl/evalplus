
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n=1, return 1
    if n == 1:
        return 1
    
    # count the number of n-digit positive integers that start with 1
    count_start_one = (n//10)+1
    
    # count the number of n-digit positive integers that end with 1
    count_end_one = (10**(n-1))//10
    
    # return the sum of count_start_one and count_end_one
    return count_start_one+count_end_one
