
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # extract number of digits in n
    num_digits = len(str(n))
    # compute count of numbers with 1 as last digit
    num_one_ends = n % 10
    # compute count of numbers with 1 as first digit
    num_one_starts = n // 10 ** (num_digits - 1)
    return num_one_ends * num_one_starts
