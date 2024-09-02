
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 4
    else:
        # 1-digit numbers
        n1 = 10**(n-1)
        # 2-digit numbers
        n2 = (9 * 10**(n-2)) * 10 + 1
        # 3-digit numbers
        n3 = n2 * 9
        return n1 + n2 + n3

