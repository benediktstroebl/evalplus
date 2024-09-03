def cycpattern_check(word1, word2):
    for i in range(len(word1)):
        if word1[i] in word2 or any(word2[j] == word1[i].rotate(1) for j in range(len(word2)-1, len(word1)-1)):
            return True
    return False