
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # a = a.lower()
    # b = b.lower()
    # b = list(b)
    # a = list(a)

    # for i in range(len(b)):
    #     if b[i:] + b[0:i] in a:
    #         return True
    # return False
    # if len(b)>=len(a):
    #     return False
    # a = list(a)
    # b = list(b)
    # for i in range(len(a)):
    #     if a[i:] + a[0:i] in b:
    #         return True
    # return False
    for i in range(len(b)):
        if b in a+a[i:]:
            return True
    return False
    
    # if len(b)>=len(a):
    #     return False
    # else:
    #     a = list(a)
    #     b = list(b)
    #     for i in range(len(a)):
    #         if b in a+a[i:]:
    #             return True
    # return False

