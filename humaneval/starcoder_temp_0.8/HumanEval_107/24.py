
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
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i, 0, -1):
            if i - j + 1 > 10 or i - j + 1 < 10:
                continue

            if i - j + 1 == 10 and j == i:
                continue

            if is_palindrome(i - j + 1):
                dp[i] += dp[j - 1]

    return dp[n - 1] % (10**9 + 7), dp[n - 1] // 2 % (10**9 + 7)

