```python
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
    return any(rotation in word1 for rotation in rotations)

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

This script includes a separate function `longest_common_subsequence` that calculates the length of the longest common subsequence between two strings, which is used to determine if the second word can be rotated to become a substring of the first word. 

The `cycpattern_check` function rotates the second word sequentially and checks if any of the rotations exist as a substring in the first word using the `any` function. 

The problem is solved programmatically using only Python and protected from issues related to case sensitivity and character-by-hour rotation by the use of the `lower` method and the `longest_common_subsequence` function. 

This solution is efficient with a time complexity of O(LCM(m, n)) where m and n represent the lengths of the two words, utilizing dynamic programming to calculate the longest common subsequence.