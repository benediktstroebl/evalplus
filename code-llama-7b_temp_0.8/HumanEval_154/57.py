
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a_len = len(a)
    b_len = len(b)
    b_rotations = b
    if b_len > a_len:
        return False
    while b_rotations != b:
        b_rotations = b_rotations[-1] + b_rotations[:-1]
        if b_rotations in a:
            return True
    return False


