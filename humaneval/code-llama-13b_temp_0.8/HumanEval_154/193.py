
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) > len(a):
        return False
    a = a.lower()
    b = b.lower()
    if len(a) == len(b):
        if b in a:
            return True
        else:
            return False

    check = False

    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            check = True
            break
        if b in a:
            for i in range(len(a)):
                if a[i:i+len(b)] == b:
                    check = True
                    break
    return check
