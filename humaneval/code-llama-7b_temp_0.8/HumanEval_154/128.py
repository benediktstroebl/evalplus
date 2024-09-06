
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
    if a_len < b_len:
        return False
    b_set = set(b)
    b_set_len = len(b_set)
    if b_len != b_set_len:
        return False
    for start_idx in range(a_len - b_len + 1):
        if set(a[start_idx:start_idx + b_len]) == b_set:
            return True
    return False
