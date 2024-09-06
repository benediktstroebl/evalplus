
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # One digit numbers
    if n == 1:
        return 1
    # Two digits numbers
    elif n == 2:
        return 2

    # Number starts with 1
    count += int('1' + '9' * (n-1) <= 10**n - 1)
    # Number ends with 1
    count += int('1' + '9' * (n-1) <= 10**n - 10)

    return count
