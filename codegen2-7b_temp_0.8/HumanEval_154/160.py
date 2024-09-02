
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(a==b):
        return True
    if(len(a)<len(b)):
        return False
    if(len(a)==len(b)):
        if(a==b):
            return True
        else:
            return False
    if(a[0]==b[-1]):
        return cycpattern_check(a[1:],b)
    else:
        return cycpattern_check(a,b[1:
