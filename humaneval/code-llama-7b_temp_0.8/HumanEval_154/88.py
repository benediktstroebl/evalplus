
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if len(a) < len(b):
        return False

    def rotate(a):
        return a[-1] + a[:-1]

    def rotated(a):
        if len(a) == 1:
            return [a]
        else:
            return [rotate(a)] + [rotate(x) for x in rotated(a[:-1])]

    return any(x in b for x in rotated(a))

