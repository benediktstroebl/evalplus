
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
    l1 = len(a)
    l2 = len(b)
    k = 0
    for i in b:
        for j in a:
            if i == j:
                k += 1
    if k == l2:
        return True
    else:
        return False
