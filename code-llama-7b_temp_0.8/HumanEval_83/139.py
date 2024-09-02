
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # first we need to find the number of digits of n
    i = 1
    count = 0
    while n >= i:
        # after we have found the number of digits of n
        # we use the number of digits to find the count of n-digit integers
        # starting or ending with 1
        num = 10 ** (n - i)
        count += (num // 10 + 1) * (num // 10)
        # the number of integers starting with 1 is the same as the number
        # of integers ending with 1
        i += 1
    return count

