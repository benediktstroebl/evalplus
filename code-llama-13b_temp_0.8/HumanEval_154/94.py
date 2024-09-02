
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
        for i in range(len(b)):
            if a[i:i+len(b)] == b:
                return True
            else:
                return False
    if len(a) > len(b):
        for i in range(len(a)-len(b)):
            if a[i:i+len(b)] == b:
                return True
            elif a[i+1:i+1+len(b)] == b:
                return True
            elif a[i+2:i+2+len(b)] == b:
                return True
            elif a[i+3:i+3+len(b)] == b:
                return True
            else:
                return False
