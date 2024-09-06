
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    assert a.isalpha()
    assert b.isalpha()

    if a:
        if not b:
            return True
        if len(a) < len(b):
            return False

        return any(b in x for x in (zip(a, a[len(a) - len(b):] + a[:len(a) - len(b)]),) * 2)
    return False

