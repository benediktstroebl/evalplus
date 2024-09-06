def cycpattern_check(word1, word2):
    rotated = ""
    word2 = word2 + word2
    for i in range(len(word2)):
        rotated = word2[i:] + word2[:i]
        if rotated.find(word1) != -1:
            return True
    return False