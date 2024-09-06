def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    # Convert the words to lower case to avoid case sensitivity issues
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Find the longest common subsequence length between the 2 words
    lcs_length = len(longest_common_subsequence(word1, word2))
    
    # Check if any rotation of the second word is a substring in the first word
    rotations = [word2[i:i+lcs_length] for i in range(0, len(word2) - lcs_length + 1)]
    return any(sub in word1 for sub in rotations)
def longest_common_subsequence(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]