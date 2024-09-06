
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # print(a,b)
    # if a in b or b in a or b in a[::-1] :
    #     return True
    # else :
    #     return False

    return b in a or b in a[1:] or b[::-1] in a or b[::-1] in a[1:]

