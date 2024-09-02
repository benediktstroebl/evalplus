
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a is b:
        return False
    a_len = len(a)
    b_len = len(b)
    for i in range(a_len):
        if a[i: a_len] == b or a[i: a_len] + a[:i] == b:
            return True
    return False
