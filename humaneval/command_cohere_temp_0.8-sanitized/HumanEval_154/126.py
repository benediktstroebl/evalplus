def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    word2 = word2 + word2
    return any(word2 in word1 for _ in range(len(word2)))