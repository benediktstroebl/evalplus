
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    result = 0
    for i in range(1,n+1):
        if i == 1 or i == n:
            result += 1
        if i == 10:
            return result
    return result
