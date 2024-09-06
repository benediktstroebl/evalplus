

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    n = len(s0)
    m = len(s1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    dp[0][n] = True
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s0[j - 1] == s1[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
