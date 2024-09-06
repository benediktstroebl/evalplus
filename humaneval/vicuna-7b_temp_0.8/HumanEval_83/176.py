
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n 1s
    ans = 0
    # n 1s in the end
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            ans += 1
    return ans
