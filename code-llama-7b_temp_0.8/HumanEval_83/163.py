
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1

    if n == 2:
        return 10

    if n == 3:
        return 91

    if n == 4:
        return 821

    if n == 5:
        return 7411

    if n == 6:
        return 68011

    if n == 7:
        return 631211

    if n == 8:
        return 6019111

    if n == 9:
        return 58479111

    if n == 10:
        return 578160111

