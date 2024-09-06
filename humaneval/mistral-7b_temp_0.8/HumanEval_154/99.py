
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = list(a)
    b = list(b)

    b.reverse()

    if a.count(b) or a.count(b[:-1]) or a.count(b[1:]) or a.count(b[2:]) or a.count(b[3:]):
        return True
    else:
        return False
