
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # First we convert n to a string
    n_str = str(n)

    # Then we calculate the number of digits n has
    length = len(n_str)

    # First we check to see if n is 1. If so, then it has 1 start and 1 end
    if n == 1:
        return 2

    # We then check to see if n is 10. If so, then it has 1 start and 0 ends
    elif n == 10:
        return 1

    # We then check to see if n is 100 or greater. If so, then it has 0 starts
    # and 1 end
    elif n >= 100:
        return 0

    # Otherwise, we return the number of digits in n times itself
    # This is because every number with n digits has (n x n) digits and
    # for every 10 digits, there is one that starts with 1
    else:
        return (length * length)

