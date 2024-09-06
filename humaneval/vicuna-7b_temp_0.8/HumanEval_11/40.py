from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = max(len(a), len(b))
    dp = [[0] * (n + 1) for _ in range(n)]
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] ^ dp[i-1][1]
        dp[i][1] = dp[i-1][1] ^ dp[i-1][0]
    return ''.join(map(str, dp))

