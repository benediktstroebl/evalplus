
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0 or len(b) == 0:
        return False
    if len(a) == 1:
        return len(a) == len(b) and a == b
    if len(b) == 1:
        return len(b) == len(a) and a == b
    if len(a) == len(b):
        return a.find(b) != -1 or a.find(b[1:] + b[0]) != -1
    return False
