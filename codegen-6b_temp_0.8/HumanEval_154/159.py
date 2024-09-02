
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for word in range(1, len(b)):
        if b in a:
            return True
        elif a in b:
            return True
        elif b in a[1:]:
            return True
        elif a in b[1:]:
            return True
        else:
            return False

