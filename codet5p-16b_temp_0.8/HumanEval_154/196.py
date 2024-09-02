
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    
    if len(a) == 0 or len(b) == 0 or len(a) < len(b):
        return False
    
    for i in range(len(b)):
        b_rotated = b[i:] + b[:i] #rotate the second word, b
        if b_rotated in a:
            return True
    return False

