
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False

    a = sorted(a)
    b = sorted(b)

    if a == b:
        return True

    for _ in range(len(b)):
        if a == b:
            return True

        b = b[-1] + b[0:len(b) - 1]
    return False

