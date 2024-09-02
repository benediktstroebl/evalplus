
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # NOTE: '1' appears at the beginning or end of an n-digit positive
    # integer iff the n-1 digit integer is a positive integer with 0 or
    # more leading zeros.
    # E.g. 1231 has 2 leading zeros so it counts as one of the starting
    # ones.
    #
    # Let's calculate how many n-digit positive integers with leading zeros
    # there are.
    # For the first digit there are 10 choices for the leading digit
    # and 9 choices for the second digit.
    # For the second digit there are 10 choices for the second leading digit
    # and 9 choices for the third digit.
    #
    # The pattern repeats so there are 10*(10^(n-2)) + 9*(10^(n-3)) starting
    # ones.
    #
    # There are 9*(10^(n-2)) + 10*(10^(n-3)) ending ones.
    #
    # Return 10*(
