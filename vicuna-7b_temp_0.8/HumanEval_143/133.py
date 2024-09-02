
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    sentence = sentence.lower()
    words = sentence.split()
    n = len(words)
    dp = [['']*n for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = words[i-1]
        for j in range(2, n):
            dp[i][j] = prime(dp[i-1][j-1]+' '+words[i])
    return dp[n-1][n-1]
