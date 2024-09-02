
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a == b:
        return True

    if not a or not b:
        return False

    if len(a) != len(b):
        return False

    str_a = a.lower()
    str_b = b.lower()

    for i in range(len(a) - len(b)):
        if str_a[i: i + len(b)] == str_b:
            return True

    return False


