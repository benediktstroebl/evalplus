
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) > len(a):
        return False
    
    if len(b) < len(a):
        return cycpattern_check(b, a[:-1]) or cycpattern_check(b, a[1:])
    
    if b == a:
        return True
    
    for c in a:
        if b.find(c)!= -1:
            return True
    
    return False








