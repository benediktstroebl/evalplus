
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    
    a = a.lower()
    b = b.lower()
    a_l = len(a)
    b_l = len(b)
    if b_l > a_l:
        return False
    else:
        for i in range(a_l):
            a_substring = a[i : a_l]
            if b == a_substring:
                return True
            else:
                a_rotate = a[i:] + a[:i]
                if b == a_rotate:
                    return True
    return False
