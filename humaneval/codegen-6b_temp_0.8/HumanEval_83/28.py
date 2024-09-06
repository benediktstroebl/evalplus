
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in range(10):
        if i == 0:
            ans += n
        elif i == 1:
            ans += n * 9
        else:
            ans += n * (9 * (9 + i - 1) - i)
    return ans
