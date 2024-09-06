
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l = len(a)
    m = len(b)
    if m > l:
        return False
    c = b
    if m == l:
        return True
    else:
        for i in range(l - m + 1, 0, -1):
            if b in (a[i:]+a[:i]):
                return True
            c = c[1:] + c[:1]
        return False
