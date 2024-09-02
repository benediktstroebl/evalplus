
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0 :
        return False 
    for x in range(1, min(len(a), len(b))):
        if b in a :
            return True
        if a in b :
            return True
        if a in a[-x:] :
            return True
        if b in a[:x] :
            return True
    return False
