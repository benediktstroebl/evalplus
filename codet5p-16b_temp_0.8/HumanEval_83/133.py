
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 10 # This is trivial, the number 10 is a 4-digit number.
    else:
        return 9 * starts_one_ends(n - 1) + 10 * ends_one_ends(n - 1)
