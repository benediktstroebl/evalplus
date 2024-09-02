
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) == 0: return True
    if len(b) > len(a): return False
    for i in range(len(a)):
        if a[i:i+len(b)] == b: return True
        if a[i:] + a[:i] == b: return True
        if a[i] == b[-1] and a[i:i+len(b)] == b[:len(b)-1]: return True
    return False
