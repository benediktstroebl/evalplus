
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    dp = 0
    arr = [0, 1, 1]
    for i in range(2, n+1):
        dp += arr[i]
        dp += arr[i-1]
    return dp
