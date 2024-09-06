
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    dp=True
    for i in range(len(a)):
        if b[i] == a[i:i+len(b[i])] or b[i] == a[i:i+len(b[i])].rot(4):
            dp = False
            break
    return dp
