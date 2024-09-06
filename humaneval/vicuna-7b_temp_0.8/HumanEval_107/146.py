
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    dp = [[0] * (10 ** 3) for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(n // 2):
        for j in range(n):
            dp[j][i] = (dp[j][i - 1] if (i - 1) % 2 == 0 else dp[j][i - 1] + dp[j - 1][i])
    return tuple(dp[j][i] for i in range(n) for j in range(n // 2))
