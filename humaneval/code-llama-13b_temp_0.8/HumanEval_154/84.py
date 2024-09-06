
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    from collections import defaultdict

    c1 = list(a)
    c2 = list(b)
    if len(c2) == len(c1):
        for i in range(len(c1)):
            c1.append(c1[0])
            del c1[0]
            if c1[:len(c2)] == c2:
                return True
    return False

