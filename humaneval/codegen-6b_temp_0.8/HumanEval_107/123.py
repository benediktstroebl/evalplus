
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
    if n == 1:
        return (1, 0)

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        low, high = 0, i // 2
        while low <= high:
            mid = (low + high) // 2
            dp[i] = min(max(dp[i-mid], dp[i-low]) + max(dp[mid+1], dp[low]) + 1, i)
            if mid + 1 <= high and mid + 1 <= i - low:
                dp[i] = min(dp[i], max(dp[i-mid-1], dp[i-low-1]) + max(dp[mid+2], dp[low]) + 1)
            if mid + 1 <= high:
                dp[i] = min(dp[i], dp[i-mid-1] + max(dp[high], dp[low]) + 1)
            if mid + 1 <= i - low:
                dp[i] = min(dp[i], dp[mid+1] + max(dp[high], dp[low]) + 1)
            low, high = mid + 1, i - low
    return (dp[-1], dp[-1] - dp[-2] - 1)
