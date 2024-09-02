
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
    if len(a)!= len(b):
        return False
    if len(a) == 0:
        return True
    if len(a) == 1:
        return a == b
    if a[0] == b[0]:
        return cycpattern_check(a[1:], b[1:])
    if a[-1] == b[-1]:
        return cycpattern_check(a[:-1], b[:-1])
    return False
