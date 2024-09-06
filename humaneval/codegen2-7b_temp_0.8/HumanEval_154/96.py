
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a is None or b is None:
        return False
    elif a.find(b)!= -1 or b.find(a)!= -1:
        return True
    elif len(a) == len(b):
        return False
    else:
        return cycpattern_check(a[1:],b) or cycpattern_check(a,b[1:])
