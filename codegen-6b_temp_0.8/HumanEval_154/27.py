
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) <= len(a):
        if b in a:
            return True
        length = len(a)
        for i in range(1, length):
            if a[i:] + a[:i] == b:
                return True
    elif len(b) > len(a):
        if a in b:
            return True
        length = len(b)
        for i in range(1, length):
            if b[i:] + b[:i] == a:
                return True
    return False

