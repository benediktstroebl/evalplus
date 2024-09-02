
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def is_rot(word1 , word2):
        if len(word1) != len(word2):
            return False
        else:
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    return False
            return True

    for i in range(len(a)):
        if is_rot(a , b[i]):
            return True
    return False
