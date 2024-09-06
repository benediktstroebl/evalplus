def cycpattern_check(word1, word2):
    """
    Checks if the second word or any of its rotations is a substring in the first word.
    Args: word1 (str): the first word
            word2 (str): the second word
    Returns: True if word2 or any of its rotations is a substring in word1, else False
    """
    word2 = word2 + word2
    return any(word2 in rotated_word for rotated_word in (word1,))