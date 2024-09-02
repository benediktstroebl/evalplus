from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    n = len(a)
    m = len(b)
    if n == 0:
        return b
    if m == 0:
        return a
    dp = [0] * (n + 1)
    for i in range(1, m+1):
        dp[i] = dp[i-1] ^ dp[i]
    return ''.join(map(lambda x: '0' if x == 0 else '1', dp))
