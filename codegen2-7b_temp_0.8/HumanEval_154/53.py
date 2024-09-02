
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a == b:
        return True
    elif len(a) < len(b):
        return cycpattern_check(a + b[len(a):], b)
    elif len(a) > len(b):
        return cycpattern_check(a[:-len(b)], b)
    else:
        return False

