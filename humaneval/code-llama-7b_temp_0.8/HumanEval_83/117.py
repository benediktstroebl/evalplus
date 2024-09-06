
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 10
    elif n == 2:
        return 8
    else:
        n1 = 9*10**(n-2)
        n2 = 10**(n-2)
        return n1*9 + n2
