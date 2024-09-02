
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not (len(a) > len(b)):
        return False
    elif not (len(a) == len(b)):
        if not ((len(a) - len(b)) == 1):
            return False
    else:
        return True

    for i in range(len(b)):
        if b[i:] in a:
            return True
    return False

