def cycpattern_check(word1, word2):
    rotations = [word2[i:] + word2[:i] for i in range(len(word2))]
    return any(sub in word1 for sub in rotations)