
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # 1st approach
    # for i in range(len(a)):
    #     if a[i:len(b)+i] == b:
    #         return True
    #     elif a[i:len(b)+i] == b[::-1]:
    #         return True
    #     else:
    #         continue
    # return False

    # 2nd approach
    if b in a or b[::-1] in a:
        return True
    return False

