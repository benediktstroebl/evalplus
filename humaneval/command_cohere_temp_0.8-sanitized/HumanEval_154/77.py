def cycpattern_check(word1, word2):
    rotated = ''
    for char in word2:
        rotated = char + rotated
        if rotated in word1: return True
    return False