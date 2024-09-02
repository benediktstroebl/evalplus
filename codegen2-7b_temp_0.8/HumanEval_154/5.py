
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def isSubstring(text, pattern):
        if len(text) < len(pattern):
            return False
        for i in range(len(pattern)):
            if text[i] == pattern[i]:
                continue
            elif text[i : i + len(pattern)] == pattern:
                return True
            else:
                continue
        return False

    return isSubstring(a, b) or isSubstring(b, a)

