
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # 1
    # b = ''.join(sorted(b))
    # if b in a:
    #     return True
    # else:
    #     return False

    # 2
    # c = list(b)
    # c.sort()
    # c = ''.join(c)
    # if c in a:
    #     return True
    # else:
    #     return False

    # 3
    # d = list(b)
    # d.sort()
    # d = ''.join(d)
    # if d in a:
    #     return True
    # else:
    #     return False
    # 4
    # b = ''.join(sorted(b))
    # if b in a:
    #     return True
    # else:
    #     return False
    # 5
    # c = list(b)
    # c.sort()
    # c = ''.join(c)
    # if c in a:
    #     return True
    # else:
    
