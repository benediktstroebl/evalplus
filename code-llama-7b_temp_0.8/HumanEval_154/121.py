
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    b_len = len(b)
    a_len = len(a)
    if a_len < b_len:
        return False
    elif a_len == b_len:
        if b in a:
            return True
    elif a_len > b_len:
        for i in range(0, a_len - b_len + 1):
            if a[i: i + b_len] == b:
                return True
    return False
