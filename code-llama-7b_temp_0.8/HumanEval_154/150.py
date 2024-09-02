
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Set a
    # Set b
    if len(a) < len(b):
        return False

    while len(a) > 0:
        # Find first rotation of a in b
        # b = b.find(a)

        # a.length < b.length
        if a == b[0:len(a)]:
            return True

        a = a[1:] + a[0]

    return False

