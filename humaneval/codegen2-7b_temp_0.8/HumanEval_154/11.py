
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = a.lower()
    l2 = b.lower()
    if len(l)!= len(l2):
        return False
    if l == l2:
        return True
    if len(l) == 1:
        return False
    if l.count(l2[0]) > 1:
        return True
    return cycpattern_check(l[1:], l2)
    

