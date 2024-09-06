
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def helper(a):
        return a[1:] + a[0]

    if not a or not b:
        return False

    if len(a) < len(b):
        a, b = b, a

    for _ in xrange(len(b)):
        if b in a:
            return True
        a = helper(a)

    return False
