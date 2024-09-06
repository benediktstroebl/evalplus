
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
    b_len = len(b)
    a_len = len(a)
    if(b_len == 0):
        return True

    if(a_len == 0):
        return False
    if(a == b):
        return True

    for i in range(a_len-b_len+1):
        if(a[i:i+b_len] == b):
            return True
        if(a[i:i+b_len] == b[::-1]):
            return True


    return False









































































































