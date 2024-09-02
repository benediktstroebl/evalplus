
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # for i in range(len(a)):
    #     if b in a:
    #         return True
    #     a = a[1:] + a[0]
    # return False

    if a == b:
        return True
    a1 = a + a
    for i in range(len(b)):
        if a1.find(b) != -1:
            return True
        a1 = a1[1:] + a1[0]
    return False

