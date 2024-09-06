
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 11
    else:
        result = 1
        result += starts_one_ends(n - 1)
        result += starts_one_ends(n - 3)
        result += 2 * starts_one_ends(n - 4)
        return result

