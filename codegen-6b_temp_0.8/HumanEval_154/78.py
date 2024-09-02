
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # if b in a or b[::-1] in a or len(a) < len(b): return False
    if len(a) < len(b): return False
    i = 1
    while i <= len(b):
        if b in a and b[-i:] in a:
            return True
        elif b[-i:] in a and b in a:
            return True
        else:
            i += 1
    return False

