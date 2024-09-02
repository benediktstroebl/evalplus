
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a[len(a)-1] == a[0]:
        if b in a:
            return True
        else:
            return False
    else:
        for i in range(len(a)-1):
            if a[i:len(a)]+a[0:i] == b:
                return True
            else:
                return False

