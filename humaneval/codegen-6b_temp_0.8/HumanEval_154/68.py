
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False
    for i in xrange(0 , len(a)):
        if b in a[i : i + len(b)]:
            return True
        if b in a[i + 1 : i + 1 + len(b)]:
            return True
        if b in a[i + 2 : i + 2 + len(b)]:
            return True
        if b in a[i + 3 : i + 3 + len(b)]:
            return True
    return False

