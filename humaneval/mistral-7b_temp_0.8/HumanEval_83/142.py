
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in range(1, n + 1):
        j = n - i
        if i == 1 and j == 0:
            ans += 1
        else:
            if i > 1 and j > 0:
                ans += 2
            elif i > 1 and j == 0:
                ans += 1
            elif i == 1 and j > 0:
                ans += 1
    return ans

