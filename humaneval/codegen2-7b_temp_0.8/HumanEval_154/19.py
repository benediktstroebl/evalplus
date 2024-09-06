
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first = set(a)
    second = set(b)

    if len(first.intersection(second)) > 0:
        return True

    if a == b:
        return True

    for i in range(len(a)):
        first = a[i:] + a[:i]
        if second.intersection(set(first)) > 0:
            return True

    return False
