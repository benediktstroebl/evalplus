
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    
    l = len(a)
    if l!= len(b):
        return False
    if l == 0:
        return True
    elif a == b:
        return True
    
    if b in a:
        return True
    for i in range(l):
        if a[i:] in a[i+1:]:
            return True
            
    return
