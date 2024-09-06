
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n1, n2 = (1, 10) if n == 1 else (10**n - 1, 10**(n-1))
    count = 0
    for i in range(n1, n2+1):
        if i == 10**n-1 or i % 10 == 1 or i % 10 == 0:
            count += 1
    return count
