
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # first find the number of n-digit numbers
    num = 1
    while n > 0:
        num *= n
        n /= 10
    # now count the number of starting 1s and ending 1s
    return num * (num // 10 // 1)
