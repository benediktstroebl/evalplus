
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
    l = len(a)
    if a[0] == b[0]:
        if len(b) == l:
            return True
        elif len(b) <= l:
            for i in range(1,l):
                if b[i] == b[0]:
                    return True
    for i in range(0,l):
        print a[i:] + b[0:i + 1] + a[0:i]
        if a[i:] + b[0:i + 1] + a[0:i] == b:
            return True
    return False
