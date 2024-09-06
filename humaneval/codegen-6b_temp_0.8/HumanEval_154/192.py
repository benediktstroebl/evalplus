
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0:
        return False
    elif len(a)==1:
        return a == b
    else:
        if a[1:] in b and (a[0]+a[1:]) in b:
            return True
        elif b[1:] in a and (a[0]+b[1:]) in a:
            return True
        else:
            return False
