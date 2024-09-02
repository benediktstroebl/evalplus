
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if a.find(b) != -1:
        return True

    i = len(b) - 1
    while i >= 0:
        if a.find(b[i:] + b[:i + 1]) != -1:
            return True
        i -= 1
    return False

