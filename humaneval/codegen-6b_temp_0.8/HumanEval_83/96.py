
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Initialize the count
    count = 0
    # Loop through the integers from 1 to N
    for num in range(1, n + 1):
        # If num ends with 1, increment the count
        if num % 10 == 1:
            count += 1
        # If num starts with 1, increment the count
        if num % 10 == 1:
            count += 1
    # Return the count
    return count

