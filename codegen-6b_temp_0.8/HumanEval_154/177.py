
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

    if m == 0:
        return True

    if m > n:
        a, b = b, a
        n, m = m, n

    for i in range(n):
        if b == a[i:]:
            return True

    return False
