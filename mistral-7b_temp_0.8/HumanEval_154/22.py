
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False
    a_sub = a[0:len(b)]
    for i in range(1, len(a) - len(b) + 1):
        if a_sub == b:
            return True
        a_sub = a_sub[1:] + a_sub[0]
    return False

