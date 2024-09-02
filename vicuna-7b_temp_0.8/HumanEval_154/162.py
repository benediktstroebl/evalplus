
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) < len(a):
        return False
    for i in range(len(b)-1):
        if a.count(b[i]) == 0:
            continue
        for j in range(len(b)-1):
            if b[j] != b[i+1] and a.count(b[j]) == 0:
                break
        else:
            return True
    return False
