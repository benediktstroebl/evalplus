
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    s = [0] * n
    for x in range(n):
        if x == 0 or x == n - 1:
            s[x] = 9
        else:
            s[x] = 9 * 10
    s[0] = 1
    return s[0] * (s[1] + 1) // 2

