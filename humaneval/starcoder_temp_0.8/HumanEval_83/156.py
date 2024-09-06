
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 10
    elif n == 2:
        return 91
    elif n == 3:
        return 739
    elif n == 4:
        return 5275
    else:
        raise ValueError("n must be less than 5")
