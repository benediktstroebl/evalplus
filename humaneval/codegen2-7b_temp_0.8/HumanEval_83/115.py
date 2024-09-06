
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(len(str(num)) == n+1 and num % 10 in [1,4,7,8] for num in range(1,10**n))

