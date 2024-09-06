
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if not n:
        return 0
    start = n if n % 10 == 1 else n % 10
    end = n % 10
    ans = 0
    if start == 1:
        ans += 9 * 10**(n-1)
    else:
        ans += start - 1
    if end == 1:
        ans += 9 * 10**(n-1)
    else:
        ans += 10**n - end + 1
    return ans
