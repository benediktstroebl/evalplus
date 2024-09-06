
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # two words : a,b
    if len(a) < len(b):
        return False

    # convert to lower case
    a = a.lower()
    b = b.lower()

    # check if a is substring of b
    if b in a:
        return True

    # check if a is substring of b[::-1]
    if b[::-1] in a:
        return True

    # check if b is substring of a
    if a in b:
        return True

    # check if b is substring of a[::-1]
    if a[::-1] in b:
        return True

    # check if b is substring of a[::-1]
    if b[::-1] in a[::-1]:
        return True

    # check if a is substring of b[::-1]
    if a[::-1] in b[::-1]:
        return True

    # check if b is substring of a[::-1]
    if b[
