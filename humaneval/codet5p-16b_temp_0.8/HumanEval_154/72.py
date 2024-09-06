
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    s1 = list(a)
    s2 = list(b)
    if len(s2) > len(s1):
        return False
    for i in range(len(s2)):
        if s1[i] == s2[0] and "".join(s1[i:i+len(s2)]) == "".join(s2):
            return True
    return False
