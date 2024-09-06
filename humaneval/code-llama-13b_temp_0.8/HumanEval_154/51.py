
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        if a == b:
            return True
    b_rotation = set()
    for i in range(len(b)):
        b_rotation.add(b[i:] + b[:i])
    return any(b_rot in a for b_rot in b_rotation)
