
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1 = len(a)
    l2 = len(b)
    if l1!= l2:
        return False
    if l2 <= 1:
        return True
    if l1 == 1:
        return False

    b = b[-1] + b[:-1]
    for i in range(1,l2-1):
        if b[i:i+l1] == a:
            return True
    return False
