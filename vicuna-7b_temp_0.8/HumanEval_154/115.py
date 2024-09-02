
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    c1 = set(a)
    c2 = set(b)
    d = len(a)
    e = d
    while e > 0:
        if c2.count(c1.pop()) == 0:
            return False
        e -= 1
    return True