
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    counter = 0
    num = 10**(n-1)
    while n>0:
        counter += int(num%10==1)
        num//=10
    return counter
