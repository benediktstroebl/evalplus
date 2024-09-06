
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If n is 1, then 11 is the only number that starts or ends with 1
    if n == 1:
        return 1

    # If n is greater than 1, then the number of n-digit numbers that start or
    # end with 1 is the number of n-1-digit numbers that start or end with 1
    # plus the number of n-1-digit numbers that start with 1 and end with 0.
    else:
        return starts_one_ends(n-1) + starts_one_ends(n-2)
