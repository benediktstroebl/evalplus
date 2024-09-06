
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(a)
    m = len(b)

    for i in range(m-1):
        if b[i] not in a:
            continue
        elif b[i+1] not in a:
            continue
        elif b[i+1] in b[0:i]:
            continue
        elif b[i+1] in a[0:i]:
            continue
        else:
            return True

    return False

