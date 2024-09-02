
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Check the cases of n=1
    if n == 1:
        return 1
    # Check the cases of n=2, n=3, n=4
    # No need to check cases of n<=4, because the number of n-digit
    # positive integers that starts or ends with 1 is less than
    # 2^n.
    # We only need to check cases of n>4.
    return (n//10) + (n%10 == 1)
