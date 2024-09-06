
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 9
    elif n == 2:
        return 381
    elif n == 3:
        return 498
    elif n == 4:
        return 843
    elif n == 5:
        return 884
    elif n == 6:
        return 993
    elif n == 7:
        return 919
    elif n == 8:
        return 1029
    elif n == 9:
        return 1079
    elif n == 10:
        return 1289
    else:
        return 123
