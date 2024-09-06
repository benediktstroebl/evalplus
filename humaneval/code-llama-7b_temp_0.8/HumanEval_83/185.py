
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Hard coded base case
    if n == 0:
        return 0
    
    # Calculate the answer recursively
    # If we start with 1, we have n-1 places for numbers.
    # We can use 10 to 9 and 0 to 9 to create 9 numbers.
    # If we end with 1, we have n-1 places for numbers.
    # We can use 10 to 9 and 1 to 9 to create 9 numbers.
    return 9 * 9 * (10 ** (n - 2))
