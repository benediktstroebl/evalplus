
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

    if len(word1) < len(word2):
        return False

    for i in range(len(word2)):
        if word2[0:len(word2)-i] in word1:
            return True

    return False
