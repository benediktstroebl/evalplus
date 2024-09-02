
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_digits = len(str(n))
    if num_digits == 1:
        return 0
    if num_digits == 2:
        return 3
    starts_one = num_digits - 1
    ends_one = 10 ** num_digits - 10 ** (num_digits - 1)
    return starts_one + ends_one
