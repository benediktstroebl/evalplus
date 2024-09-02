
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return cycpattern_check(b,a)
    a = list(a)
    for i in range(len(b)):
        for j in range(len(b)):
            b1 = a[:i]+a[i+j:]
            if b1 == b:
                return True
            else:
                pass
    return False
