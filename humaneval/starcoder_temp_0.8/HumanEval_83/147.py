
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Strategy: for each n-digit number, there is a 50% chance of starting
    # with 1 and a 50% chance of ending with 1.
    #
    # An alternative strategy would be to iterate through the list of
    # all numbers up to n-digit numbers and count how many of them start
    # and end with 1.
    return n * 10**(n-1)

