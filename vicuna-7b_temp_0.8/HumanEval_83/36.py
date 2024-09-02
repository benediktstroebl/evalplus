
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n <= 1:
        return 1
    # sub case
    elif n % 2 != 0:
        return 1 + starts_one_ends(n//2)
    else:
        return 1 + starts_one_ends(n//2) + starts_one_ends(n//2)
