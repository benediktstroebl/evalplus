
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not a or not b:
        return False
    if len(b) != len(a):
        return False
    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i:i+len(b)] == b) or (a[i+len(b):i+len(b)] == b):
                return True
    return False