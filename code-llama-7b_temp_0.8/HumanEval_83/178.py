
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # how many numbers end with 1?
    end_with_one = 10 ** (n - 1)

    # how many numbers start with 1?
    start_with_one = 10 ** (n - 1) - 1

    return end_with_one + start_with_one

