
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return any(subword in a for subword in [a, a[1:] + a[0], a[2:] + a[:2], a[-1] + a[0:-1], a[-2:] + a[0:-2], a[-3:] + a[:3], a[-4:-2] + a[:2] + a[0:2]])
