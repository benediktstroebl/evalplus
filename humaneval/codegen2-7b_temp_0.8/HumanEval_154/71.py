
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    a = a.split("")
    b = b.split("")
    if (a == b):
        return True
    if (a == list(reversed(b))):
        return True
    for i in range(0,len(a)):
        if (a == b[i:len(a)]):
            return True
    return False

