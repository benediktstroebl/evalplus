
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # use 1000000000 as a large enough number to handle any n
    # use 1000000000 % x to find the remainder when 1000000000 is divided
    # by x, and then check if that remainder is 0 or 1
    # this is equivalent to checking if 1000000000 / x is an integer
    # or 1000000000 / x - 1 is odd
    # since the largest number that fits in a int is 2000000000-1 (999999999),
    # we can just check if x is odd or even
    count = 0
    for i in range(1, n+1):
        # check if i starts with 1
        if i == 1 or i % 10 == 1 or i % 100 == 1 or i % 1000 == 1:
            count += 1
        # check if i ends with 1
        elif i % 10 == 1 or i % 100 == 1 or i % 1000 == 1:
            count += 1
    return count
