
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return a in b or a[1:] in b or a[2:] + a[:2] in b or a[3:] + a[:3] in b or a[:-1]+a[-1]+a[1:-1] == b or a[1:]+a[:-1]+a[2:]in b or a[:-1]+a[-2]+a[1:] in b or a[:-1]+a[-3]+a[1:]in b
