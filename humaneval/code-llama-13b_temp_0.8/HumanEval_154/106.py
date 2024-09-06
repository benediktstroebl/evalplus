
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(0,len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return True
        else:
            pass
        if a[i:i+len(b)] == b[len(b)-1::]+b[:-1]:
            return True
        else:
            pass
    return False
        
