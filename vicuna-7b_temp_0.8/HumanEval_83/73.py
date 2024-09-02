
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Initialize a count variable
    count = 0
    
    # Iterate through n-digit positive integers
    for i in range(1, n+1):
        # Check if the number starts with 1
        if i == 1:
            count += 1
        # Check if the number ends with 1
        elif i % 10 == 1:
            count += 1
    
    return count
