
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == len(b):
        return a in b
    if len(b) > len(a):
        for i in range(0, len(b) - len(a) + 1):
            if a in b[i:len(b)]:
                return True
        return False
    else:
        for i in range(0, len(a) - len(b) + 1):
            if b in a[i:len(a)]:
                return True
        return False

