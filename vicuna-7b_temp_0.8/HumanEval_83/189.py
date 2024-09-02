
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n-1, because the last digit of the number is not considered in this problem
    # 0, because 0-digit numbers are not considered here
    # 1, because there is only one 1-digit number that starts with 1
    return n-1-1+1
