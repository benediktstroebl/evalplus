
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    """
    This function is called for every pair of words.
    If one of the words is a substring of the other word,
    it needs to return True, otherwise False

    """
    if b == a or b in a:
        return True
    elif b in a + a:
        return True

    if len(b) < len(a):
        return False

    m = len(b)
    for i in range(m):
        if b[i:] + b[:i] == a:
            return True
        if b[i:] + b[:i] == a + a:
            return True

    return False

