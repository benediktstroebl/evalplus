def cycpattern_check(word1, word2):
    rotations = [word2[i:] + word2[:i] for i in range(len(word2))]
    return any(word2 in word1 or rotation in word1 for rotation in rotations)