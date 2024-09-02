
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If n is 1, it is one, so return 1.
    if n == 1:
        return 1
    # Create a new variable called left and initialize it with one.
    left = 1
    # Create a new variable called right and initialize it with zero.
    right = 0
    # Create a new variable called count and initialize it with 1.
    count = 1
    # If n is greater than one, iterate through the n digits.
    for i in range(2, n+1):
        # Add the current digit to the left variable.
        left = left * i
        # Subtract the current digit from the right variable.
        right = right - i
        # Add the count of the number of digits that start with one to the count.
        count = count + left + right
    # Return the count.
    return count
