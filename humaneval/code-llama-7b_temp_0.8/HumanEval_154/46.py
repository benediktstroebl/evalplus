
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # if len(b) != len(a):
    #     return False
    # if a == b:
    #     return True

    # c = a + a
    # for i in range(0,len(b)):
    #     if a[i:i+len(b)] == b:
    #         return True
    # return False


    if a == b:
        return True

    c = a + a
    for i in range(0, len(b)):
        if c[i:i+len(b)] == b:
            return True
    return False
