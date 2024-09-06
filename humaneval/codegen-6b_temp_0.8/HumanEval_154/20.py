
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # convert to lower case
    a = a.lower()
    b = b.lower()
    # check if we have a rotational match
    if a[:len(b)] == b or a[-len(b):] == b or a == b:
        # we've found a match
        return True
    # check for a unique match of substrings
    for i in xrange(len(b)):
        if a.find(b[i:]) != -1:
            return True
    return False

