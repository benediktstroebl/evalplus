
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Make sure n is positive
    assert n > 0, "n must be positive"

    # Calculate how many 1s there are in n
    num_ones = n + n - 1

    # Calculate how many n-digit numbers there are
    num_digits = 10 ** n

    # Calculate the number of numbers that start or end with 1
    return num_digits - (num_digits - num_ones)
