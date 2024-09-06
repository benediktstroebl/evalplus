
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(a)
    pattern = b * 2
    for i in range(n):
        if a.find(b) != -1:
            return True
        else:
            pattern = pattern[1] + pattern[0]
            if a.find(pattern) != -1:
                return True
            elif b == pattern:
                return False
