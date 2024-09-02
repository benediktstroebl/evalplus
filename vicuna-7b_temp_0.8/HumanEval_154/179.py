
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
    for i in range(len(b)):
        if a.endswith(b[i:]) or a.endswith(str(b[i])+str(b[i+1])) or b[i:].endswith(a) or b[i:].endswith(str(a)+str(a[1])):
            return True
    return False