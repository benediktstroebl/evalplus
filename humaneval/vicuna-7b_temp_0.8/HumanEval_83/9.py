
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Initialize the count of 1-start and 1-end numbers
    count_1_start = 0
    count_1_end = 0
    
    # Loop through the range of n-digit positive integers
    for i in range(1, n + 1):
        # Count the number of 1-start numbers
        for j in range(i, n + 1):
            if j == 1:
                count_1_start += 1
            elif j % 2 == 1:
                count_1_start += 1
    
        # Count the number of 1-end numbers
        for j in range(i, n + 1):
            if j == 1:
                count_1_end += 1
            elif j % 2 == 1:
                count_1_end += 1
    
    return count_1_start + count_1_end
