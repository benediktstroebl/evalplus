def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(word1) < len(word2):
        return False
    word2 = word2 + word2
    return any(word2.startswith(prefix) for prefix in (word2, ) if prefix)