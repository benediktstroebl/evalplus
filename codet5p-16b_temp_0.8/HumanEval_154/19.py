
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a = list(a)
    b = list(b)
    if len(b) == 0:
        return True
    if len(a) < len(b):
        return False
    for i in range(len(b)):
        if b in a:
            return True
        if b[0] not in a:
            return False
        b.append(b[0])
        del b[0]
    return False



