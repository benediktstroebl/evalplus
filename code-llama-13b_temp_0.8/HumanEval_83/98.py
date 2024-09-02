
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # One case: first digit is 1.
    # n - 1 possibilities to fill the rest of the digits.
    num_one = 10 ** (n - 1)
    # One case: last digit is 1.
    # n - 1 possibilities to fill the rest of the digits.
    num_last = 10 ** (n - 1)
    return num_one + num_last

