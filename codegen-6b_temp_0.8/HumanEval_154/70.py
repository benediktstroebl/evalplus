
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
        a,b = b,a
    a,b = a.lower(),b.lower()
    for x in xrange(0,len(b)+1):
        b1 = b[x:]+b[:x]
        if b1 in b:
            return True
    return False 
