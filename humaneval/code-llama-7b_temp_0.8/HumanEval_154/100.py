
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    check = a.split()
    chk = b.split()
    a_len = len(check)
    b_len = len(chk)
    if a_len > b_len:
        if any(chk in check[i:] for i in range(a_len)):
            return True
        else:
            return False
    else:
        if any(chk in check for i in range(b_len)):
            return True
        else:
            return False



