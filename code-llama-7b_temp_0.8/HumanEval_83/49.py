
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # Handle the base case (1-digit numbers)
    if n == 1:
        count = 2
    # If n > 1, n must be between 2 and 9.  In this case, only the first
    # digit can be 1.  The last digit can be either 1 or 9.
    else:
        count += (10 - n)
        # The last digit can't be 0 or 9 since that's not valid for a 
        # n-digit number.
        count += (9 - n)
    return count
