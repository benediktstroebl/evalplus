
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # check if a and b have same len
    if len(a) != len(b):
        return False
    # check if b is substring of a
    for i in range(len(b)):
        if a.find(b[i:i+len(b)]) != -1:
            return True
    # check if any of the rotations of b is substring of a
    for i in range(len(b)):
        rot = b[i:] + b[:i]
        if a.find(rot) != -1:
            return True
    return False
