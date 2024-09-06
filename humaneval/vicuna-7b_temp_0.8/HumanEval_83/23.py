
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n is 1, return 1
    if n == 1:
        return 1
    # if n is odd, return 2
    if n % 2 == 1:
        return 2
    # check the digits of n
    # we will count all the n-digit numbers that start or end with 1
    # the first digit must be 1 or n % 10
    count = 0
    digit = n % 10
    if digit == 1:
        count += 1
    # if n % 10 is odd, we can't check digit 1
    while digit > 0:
        digit = n % 10
        if digit == 1:
            count += 1
        if digit > 1:
            digit -= 1
            n //= 10
    return count
