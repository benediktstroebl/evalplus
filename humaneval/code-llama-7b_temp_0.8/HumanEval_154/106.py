
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # returns True if string s is a substring of any rotation of t
    def is_substring(s, t):
        l_t = len(t)
        for i in range(l_t):
            if s in t[i:] + t[:i]:
                return True
        return False

    return is_substring(b, a)


