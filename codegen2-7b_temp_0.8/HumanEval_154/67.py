
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
    if len(a) < len(b):
        return cycpattern_check(b, a)
    if a[0]!= b[0]:
        return False
    if a[len(a)-1]!= b[len(b)-1]:
        return False
    if len(a) == len(b):
        return True
    if a in b:
        return True
    if b in a:
        return True
    return cycpattern_check(b, a[1:]) or cycpattern_check(a, b[1:
