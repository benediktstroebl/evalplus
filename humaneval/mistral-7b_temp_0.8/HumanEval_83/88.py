
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Find the number of digits in n
    n_digits = len(str(n))

    # If n has only one digit, return 1
    if n_digits == 1:
        return 1

    # Otherwise, recurse on the lower and upper halves of the number
    return starts_one_ends(n // 10) + starts_one_ends(n // 10 * 10 + 1)
