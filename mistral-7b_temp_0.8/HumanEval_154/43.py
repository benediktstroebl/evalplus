
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    for i in range(len(b)):
        if b[i] not in d:
            d[b[i]] = 1
        else:
            d[b[i]] += 1

    for i in range(len(b)):
        if d.get(b[i]) is None:
            return False
        else:
            d[b[i]] -= 1
    for i in range(len(b)):
        if d[b[i]] is not None:
            return False
    return True
