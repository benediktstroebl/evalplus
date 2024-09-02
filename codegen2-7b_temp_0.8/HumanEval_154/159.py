
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if (a==b):
        return True
    if (len(a)<2 or len(b)<2):
        return False
    if (a[:2]!=b[:2]):
        return False
    return cycpattern_check(a[2:],b[1:]) or cycpattern_check(a[1:],b[2:]) or cycpattern_check(a[2:],b[2:
