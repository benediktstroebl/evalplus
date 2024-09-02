
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # we only need to check for the case when n is 1 or 2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n % 10 == 1:
        return 1
    else:
        # n is not 1 or 2 and is not divisible by 10
        return 0
