
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 8
    elif n == 2:
        return 8*9
    else:
        return (8*9+7+1)*(9**(n-2)-1)

