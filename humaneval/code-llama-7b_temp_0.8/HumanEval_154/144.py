
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(a == b):
        return True

    a_length = len(a)
    b_length = len(b)
    if(a_length < b_length):
        return False

    for x in range(b_length,a_length+1):
        cyc = a[x-b_length:x]
        if(cyc == b):
            return True

    return False

