
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # First, get the number of n-digit numbers that end in 1.
    # We'll do this by finding the number of (n - 1)-digit numbers
    # that end in 0 or 1.
    ending_in_one = (n - 1) * 10 + 1

    # Each of these has 2 choices for its 0 or 1 ending.
    # The first digit can be 0 or 1, but not 2, so we have:
    ending_in_one *= 2

    # Then, the remaining (n - 2) digits can be any number of any digits
    # so we have:
    ending_in_one *= (10 ** (n - 2))

    # We can now find the number of numbers starting in 1 by subtracting
    # the number ending in 0 or 1 from the number ending in 1.
    starting_in_one = ending_in_one - (n - 1) * 10

    return (starting_in_one + ending_in_one)
