
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a_chars = sorted(a)
    b_chars = sorted(b)

    if len(a_chars) != len(b_chars):
        return False

    for index, i in enumerate(a_chars):
        if b_chars[index] != i:
            return False
    return True

