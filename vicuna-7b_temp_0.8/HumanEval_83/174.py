
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 2 ways for n=1, return 1
    if n==1:
        return 1

    # 3 ways for n=2, return 2
    if n==2:
        return 2

    # n-1 cases for n>=3, return n-1
    return n-1
