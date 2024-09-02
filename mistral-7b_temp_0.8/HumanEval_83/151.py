
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Takes a positive integer n as argument and returns the count of the
    # numbers of n-digit positive integers that start or end with 1.
    # Assume the numbers are at most 1000 digits long.
    #
    # >>> starts_one_ends(1)
    # 9
    # >>> starts_one_ends(2)
    # 99
    # >>> starts_one_ends(3)
    # 999
    # >>> starts_one_ends(10)
    # 9999999999
    # >>> starts_one_ends(100)
    # 9999999999999999999
    # >>> starts_one_ends(1000)
    # 9999999999999999999999999999999999999999999999999999999999999
