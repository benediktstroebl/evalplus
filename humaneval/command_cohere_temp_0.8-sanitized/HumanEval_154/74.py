def cycpattern_check(word1, word2):
    """
    You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word.
    """
    if word1 == word2:
        return True
    if len(word1) != len(word2):
        return False
    letters_map = {letter: word2.count(letter) for letter in set(word2)}
    return any(letter in letters_map and letters_map[letter] > 1 for letter in word1)