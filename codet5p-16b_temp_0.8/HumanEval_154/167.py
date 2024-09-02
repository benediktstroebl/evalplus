
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    len_a = len(a)
    len_b = len(b)
    if len_a == len_b:
        return False
    if a in b:
        return True
    if b in a:
        return True
    for i in range(0,len_a):
        if a[i:len_a] in b:
            return True
    for i in range(0,len_b):
        if b[i:len_b] in a:
            return True
    return False
