
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    p = len(b)
    n = len(a)
    if (n - p) < 0:
        return False

    for i in range(p):
        if b == a[i : i+p]:
            return True
        if b == a[n-p+i:n+i] :
            return True
    
    return False
