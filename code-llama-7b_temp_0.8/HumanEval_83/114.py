
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digits = len(str(n))
    return sum(
        [int(str(10 ** (digits - 1))[i] == '1') for i in range(digits - 1)]
    )

