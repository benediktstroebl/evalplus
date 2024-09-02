
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    res = False
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        if b in a:
            res = True
    else:
        if a in b:
            res = True
    for i in range(len_b - 1):
        b = b[-1] + b[:-1]
        if b in a:
            res = True
            break
    return res

