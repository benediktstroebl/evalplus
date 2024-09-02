
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1=len(a)
    l2=len(b)
    s2=""
    for i in range(l1):
        s2=s2+b[i%l2]
    s2=s2[l1:]
    if s2 in a:
        return True
    else:
        return False

