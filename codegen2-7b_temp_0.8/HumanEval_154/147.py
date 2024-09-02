
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if (a == b):
        return True
    if len(a)!= len(b):
        return False
    if (a == b[0:2]) or (a[-2:] == b) or (a[:2] == b[2:]):
        return True
    for i in range(1, len(a)):
        if a[i:i+2] == b[0:2]:
            return True
        if a[-i:] == b:
            return True
        if a[:i] == b[2:]:
            return True
    
