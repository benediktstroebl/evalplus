
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    import collections
    def word_rotation(a,b):
        if collections.Counter(a) == collections.Counter(b):
            return True
        else:
            return False

    return word_rotation(a,b) or word_rotation(a,b[::-1])

