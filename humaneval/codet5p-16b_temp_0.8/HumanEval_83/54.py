
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert n > 0, "Please provide a positive integer"
    ans = 0
    for i in range(n-1, -1, -1):
        if i == 0:
            ans += (n-1) * (n-2) // 2
        else:
            ans += (n-i) * (n-i-1) // 2
    return ans
