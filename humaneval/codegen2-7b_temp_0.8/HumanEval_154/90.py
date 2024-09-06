
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a_len = len(a)
    b_len = len(b)
    for i in range(0,b_len):
        if b[0:i] == a[-i:]:
            return True
    if b_len<=a_len:
        for i in range(0,a_len):
            if b[0:b_len-i] == a[-i:a_len]:
                return True
    return False



