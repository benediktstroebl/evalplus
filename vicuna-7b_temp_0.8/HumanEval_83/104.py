
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If n is 1, return 1
    if n == 1:
        return 1
    
    # If n is 2, return 2
    if n == 2:
        return 2
    
    # If n is 3, return 4
    if n == 3:
        return 4
    
    # If n is 4, return 7
    if n == 4:
        return 7
    
    # If n is 5, return 12
    if n == 5:
        return 12
    
    # Calculate the count of numbers of n-digit positive integers
    # that start with 1 and end with 1
    count_start_with_1 = (n//10)*(n//10+1)
    count_end_with_1 = (n//10)
    
    # Calculate the count of numbers of n-digit positive integers
    # that start with 1 and end with 9
    count_end_with_9 = (n//10)
    
    # Return the sum of the count of numbers of n-digit positive integers
    # that start with 1 and end with 1 and the count of numbers of n-digit
    # positive integers that start with 1 and end with 9
    return count_start_with_1 + count_end_with_9
