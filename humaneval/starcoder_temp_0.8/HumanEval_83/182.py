
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    ans = 0
    for i in range(1, 10 ** (n - 1), 10):
        if i == 1:
            ans += 1
        elif i == 10 ** (n - 1):
            ans += 1
        elif str(i)[0] == "1" or str(i)[-1] == "1":
            ans += 1
    return ans
