
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return (a.find(b) >= 0 or
            (len(b) == 2 and a[1:] + a[0] == b) or
            (len(b) == 3 and a[2:] + a[:2] == b) or
            (len(b) == 4 and a[3:] + a[:3] == b) or
            (len(b) == 5 and a[4:] + a[:4] == b) or
            (len(b) == 6 and a[5:] + a[:5] == b) or
            (len(b) == 7 and a[6:] + a[:6] == b) or
            (len(b) == 8 and a[7:] + a[:7] == b) or
            (len(b) == 9 and a[8:] + a[:8] == b) or
            (len(b) == 10 and a[9:] + a[:9] == b))

    # return (a.find(b) >= 0 or
    #         (a[:] and a[1:] + a[0] == b) or
    #         (a[:] and a[2:] + a[:2] == b) or
    #         (a[:] and a[3:] + a[:3] == b) or
    #         (a[:] and a[4:] + a[:4] == b) or
    #         (a[:] and a[5:] + a[:5] == b) or
    #         (a[:] and a[6:] + a[:6] == b) or
    #         (a[:] and a[7:] + a[:7] == b) or
    #         (a[:] and a[8:] + a[:8] == b) or
    #         (a[:] and a[9:] + a[:9] == b))


