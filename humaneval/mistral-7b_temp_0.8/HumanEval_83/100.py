
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    l = len(str(n))
    a = 0
    b = 0
    if l == 1:
        return 2
    if l == 2:
        return 4
    if l == 3:
        return 6
    if l == 4:
        return 8
    if l == 5:
        return 10
    if l == 6:
        return 12
    if l == 7:
        return 14
    if l == 8:
        return 16
    if l == 9:
        return 18
    if l == 10:
        return 20
    if l == 11:
        return 22
    if l == 12:
        return 24
    if l == 13:
        return 26
    if l == 14:
        return 28
    if l == 15:
        return 30
    if l == 16:
        return 32
    if l == 17
