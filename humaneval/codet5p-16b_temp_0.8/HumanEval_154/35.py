
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    word1 = a.lower()
    word2 = b.lower()
    word1_len = len(word1)
    word2_len = len(word2)
    rotations = []
    if word1_len < word2_len:
        return False
    for i in range(word1_len):
        temp = word1[i:] + word1[:i]
        rotations.append(temp)
    for each in rotations:
        if word2 in each:
            return True
    return False

