def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(word1) < len(word2):
        return False
    if word2 in word1:
        return True
    for i in range(len(word2)):
        if word2[i:] in word1 or word2[:i] in word1:
            return True
    return False