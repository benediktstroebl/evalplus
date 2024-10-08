
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return (starts_one_ends(n-1) * 9) + (n*10 - starts_one_ends(n-1) * 9)
