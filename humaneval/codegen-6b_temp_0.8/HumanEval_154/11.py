
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a:
        return True
    elif len(a) < len(b):
        s1 = a
        s2 = b
    else:
        s1 = b
        s2 = a
    if s1[:len(s2)] == s2:
        return True
    elif s2[:len(s1)] == s1:
        return True
    else:
        return False
