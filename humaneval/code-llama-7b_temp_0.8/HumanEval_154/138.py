
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    #your code goes here
    if a == b:
        return False
    if len(a) != len(b):
        return False
    if len(b) == 1:
        return False
    if len(a) < 2:
        return False
    x = 0
    y = len(a) - 1
    while x < y:
        z = 0
        while z < len(b):
            a = a[x:] + a[:x]
            if a == b:
                return True
            else:
                z += 1
        x += 1
    return False
