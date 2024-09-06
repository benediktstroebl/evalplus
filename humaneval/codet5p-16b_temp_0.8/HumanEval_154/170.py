
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a1 = a
    b1 = b
    while a!= b and len(a) >= len(b):
        a = a[1:] + a[0]
    while a!= b and len(b) >= len(a):
        b = b[1:] + b[0]
    if a == b:
        return True
    else:
        return False


