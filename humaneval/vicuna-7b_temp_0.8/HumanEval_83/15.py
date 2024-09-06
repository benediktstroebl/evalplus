
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n <= 1:
        return 1

    # handle the case when n is 2
    if n == 2:
        return 2

    # handle the case when n is 3
    if n == 3:
        return 3

    # loop through the rest of the digits in the number
    for digit in str(n):
        # handle the case when n ends with 1
        if digit == '1':
            count += 1

        # handle the case when n starts with 1
        if digit == '1' and n % 10 > 0:
            count += 1

        # handle the case when n is a multiple of 10
        if n % 10 == 0:
            count += n // 10

    return count
