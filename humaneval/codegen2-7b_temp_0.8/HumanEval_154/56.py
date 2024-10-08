
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0:
        return False
    if len(b) == 0:
        return True
    if a.find(b) > -1:
        return True
    if cycpattern_check(a[1:]+a[0],b) or cycpattern_check(a+a[1:],b):
        return True
    return False
