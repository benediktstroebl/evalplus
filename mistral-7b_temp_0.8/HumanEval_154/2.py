
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a.find(b)>=0:
        return True
    elif len(a)<len(b):
        return False
    else:
        for i in range(1, len(a)-len(b)+1):
            if a.find(b[i-1:]+b)>=0:
                return True
        return False

