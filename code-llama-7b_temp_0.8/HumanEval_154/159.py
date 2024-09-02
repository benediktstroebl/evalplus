
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) > len(b):
        return cycpattern_check(b, a)

    if len(a) == 0 or len(b) == 0 or len(b) > 26:
        return False

    check = len(a) % len(b)
    if check == 0:
        return a.find(b) != -1
    else:
        a = a + a
        return a.find(b) != -1


