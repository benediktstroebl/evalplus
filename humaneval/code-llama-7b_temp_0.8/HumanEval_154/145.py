
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # for i in b:
    #     if len(a)<len(b):
    #         return False

    #     for j in range(len(b)):
    #         if a[j:j+len(b)] == b:
    #             return True
    # return False

    if len(a)<len(b):
        return False
    elif len(a)%len(b) == 0 and a == b*int(len(a)/len(b)):
        return True

    for i in range(len(b)):
        # rotating the string
        a = a[1:]+a[0]
        if a == b*int(len(a)/len(b)):
            return True
    return False


