
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def cycle(s):
        if s in s[::-1]:
            return True, s

        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False, s[-1] + s[:-1]

        return True, s[-1] + s

    return cycle(a)[0] and cycle(b)[0]
