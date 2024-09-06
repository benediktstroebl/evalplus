from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = len(a)
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        if a[i-1] == '1':
            dp[i] = dp[i-1] ^ dp[i-2]
        else:
            dp[i] = dp[i-1]
    for i in range(n):
        if dp[i] == 1:
            return '1' * i
        else:
            return '0' * i

