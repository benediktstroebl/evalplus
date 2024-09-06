
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If n is 0, then there is 0 such number
    if n <= 0:
        return 0
    # If n is 1, then there are 10 such numbers
    if n == 1:
        return 10
    # If n is 2, then there are 9 such numbers
    if n == 2:
        return 9
    # If n is 3, then there are 8 such numbers
    if n == 3:
        return 8
    # If n is 4, then there are 7 such numbers
    if n == 4:
        return 7
    # If n is 5, then there are 6 such numbers
    if n == 5:
        return 6
    # If n is 6, then there are 5 such numbers
    if n == 6:
        return 5
    # If n is 7, then there are 4 such numbers
    if n == 7:
        return 4
    # If n is 8, then there are 3 such numbers
    if n == 8:
        return 3
    # If n is 9, then there are 2 such numbers
    if n == 9:
        return 2
    # Otherwise, there is only one such number
    return 1
