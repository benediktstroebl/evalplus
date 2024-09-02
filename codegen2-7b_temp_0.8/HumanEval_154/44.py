
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    word1 = a
    word2 = b
    if word1 in word2:
        return True
    if word2 in word1:
        return True
    for i in range(1,len(word1)):
        if word1[-i:] in word2:
            return True
    for i in range(1,len(word2)):
        if word2[-i:] in word1:
            return True
    
