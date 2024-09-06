
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 and len(b) == 0:
        return True
    elif len(b) == 0:
        return True
    elif len(a) < len(b):
        return cycpattern_check(a, a[len(b):]) or cycpattern_check(a, a[:len(b)])
    elif len(a) == len(b):
        return a == b
    else:
        return cycpattern_check(a[1:], b) or cycpattern_check(a[:len(b)-1], b
