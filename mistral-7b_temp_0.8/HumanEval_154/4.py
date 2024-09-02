
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) == 0:
        return False
    if len(b) == 0:
        return False

    #for s in range(len(a)):
    #    if a[s:] == b:
    #        return True

    # for s in range(len(b)):
    #     if a == b[:-s]:
    #         return True

    # for s in range(len(a)):
    #     if a[:-s] == b:
    #         return True

    # for s in range(len(b)):
    #     if b == a[:-s]:
    #         return True


    # checking whether b is a substring of a
    for i in range(len(b)):
        if a.find(b[i:]) != -1:
            return True


    # checking whether a is a substring of b
    for i in range(len(a)):
        if b.find(a[i:]) != -1:
            return True

    return False


