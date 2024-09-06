def cycpattern_check(word1, word2):
    """
    You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(word1) < len(word2):
        return False
    if word2 in word1:
        return True
    # Iterate over possible rotations of word2 and check if any of them match against word1
    for i in range(len(word2)):
        rotated_word2 = word2[i:] + word2[:i]
        if rotated_word2 in word1:
            return True
    return False