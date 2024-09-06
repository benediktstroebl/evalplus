
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
    # dp[i][j] is the number of odd and even integer palindromes
    # that are in range(i, j+1) inclusive
    # For dp[i][j], we can see:
    #   Case 1: dp[i][j] = dp[i][j - 1] if is_palindrome(nums[i][j])
    #   Case 2: dp[i][j] = dp[i + 1][j - 1] + dp[i][j - 1] - dp[i + 1][j] if is_palindrome(nums[i][j]) and nums[i][j] != nums[i + 1][j - 1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 1
    for start in range(n):
        for end in range(1, n - start + 1):
            if start == end:
                if is_palindrome(nums[start][end]):
                    dp[start][end] = 1
            else:
                if is_palindrome(nums[start][end]):
                    dp[start][end] = dp[start + 1][end - 1] + dp[start][end - 1] - dp[start + 1][end]
    result = []
    for i in range(n):
        result.append(dp[i][n])
    return tuple(result)

