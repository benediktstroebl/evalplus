
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # check if b is a substring in a
    if b in a:
        return True

    # check if b or its rotations are a substring in a
    for rot_b in _cyc_rot(b):
        if rot_b in a:
            return True

    return False
