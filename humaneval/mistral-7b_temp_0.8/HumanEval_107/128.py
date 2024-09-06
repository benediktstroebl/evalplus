
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
    # using dynamic programming
    # for even
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        if i % 2 == 1:
            dp[i] = 2 * dp[i // 2]

    # for odd
    dp_odd = [0] * (n + 1)
    dp_odd[1] = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp_odd[i] = 2 * dp_odd[i // 2]
        if i % 2 == 1:
            dp_odd[i] = dp_odd[i // 2] + dp_odd[(i - 1) // 2]

    return dp[-1], dp_odd[-1]

