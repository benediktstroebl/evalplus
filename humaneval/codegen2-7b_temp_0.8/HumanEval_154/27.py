
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)!= len(b):
        return False

    if b in a:
        return True

    l = len(b)

    if len(a) < l:
        return False

    if a[:l] == b:
        return True

    if a[l:] == b:
        return True

    if a[:l -1] == b:
        return True

    if a[l -1:] == b:
        return True

    return
