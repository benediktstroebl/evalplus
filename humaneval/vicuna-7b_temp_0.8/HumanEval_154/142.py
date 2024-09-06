
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        for i in range(len(a)):
            if b[i:i+len(b)] in a:
                return True
        return False
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if (b[i:j]+b[j:]) in a:
                return True
    return False
