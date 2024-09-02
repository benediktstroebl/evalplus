
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    n=n-1
    if n==0:
        return 2
    if n==1:
        return 3
    return n*3+2

