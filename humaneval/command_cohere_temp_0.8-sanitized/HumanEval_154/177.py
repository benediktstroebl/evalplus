def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    word1 = word1.lower()
    word2 = word2.lower()
    rotations = [word2, word2[1:] + word2[:1], word2[2:] + word2[:2], word2[3:] + word2[:3]]
    return any(sub in word1 for sub in rotations)