
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Counts of numbers of 1-digit integers
    ones_start_end = n-1
    # Counts of numbers of n-digit integers where n > 1
    ones_start_end += n-1
    return ones_start_end
