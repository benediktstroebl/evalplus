
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # str2 = a[1:] + a[0]
    # str3 = b[1:] + b[0]

    # if str2 in b or str3 in b:
    #     return True
    # return False
    a = a + a
    if b in a:
        return True
    return False
