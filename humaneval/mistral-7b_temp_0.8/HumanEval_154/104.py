
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    i = 0
    l1 = len(a)
    l2 = len(b)
    for i in range(l1):
        if a[i:l1] == b:
            return True
        elif a[i:l1] == b[0:l2-1]:
            return True
        elif a[i:l1] == b[1:l2]:
            return True
        elif a[i:l1] == b[2:l2-1]:
            return True
        else:
            continue


    return False



