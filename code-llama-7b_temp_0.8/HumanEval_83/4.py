
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 3 == 1:
            return 3
        elif n % 3 == 2:
            return 3
        else:
            return 3
