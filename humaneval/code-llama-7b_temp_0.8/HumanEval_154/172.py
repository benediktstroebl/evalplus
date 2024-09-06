
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    len1 = len(a)
    len2 = len(b)
    if len1 < len2:
        return False
    for i in range(len1 - len2 + 1):
        if b in a[i:] or a[i:] in b or a[i:i + len2] in b:
            return True
    return False


