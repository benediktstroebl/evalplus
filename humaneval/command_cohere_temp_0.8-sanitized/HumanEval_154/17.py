def cycpattern_check(word1, word2):
    rotations = [word2[i:i+len(word2)//2] for i in range(0, len(word2), len(word2)//2)]
    return any(sub in word1 for sub in rotations)