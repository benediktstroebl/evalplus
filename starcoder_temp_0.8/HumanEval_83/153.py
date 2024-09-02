
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(1, n):
            num = int(str(j) + '1' * i + str(j))
            ans += 1
    return ans

