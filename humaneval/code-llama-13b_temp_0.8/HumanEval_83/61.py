
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        raise ValueError('Expected a positive integer.')

    # The last digit is fixed, so make it '1'
    last_digit = 1

    # The first digit can be either '1' or '2', which results in 2 possibilities
    # for the first digit. The rest of the digits are filled by '1' to make
    # n-digit number.
    return (10 ** (n - 2)) * 2
