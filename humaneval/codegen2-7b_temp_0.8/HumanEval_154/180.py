
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def check_match(pattern, word):
        start = 0
        while start < len(pattern):
            if pattern[start:start+len(pattern)] == word[:len(pattern)]:
                return True
            start += 1
        return False

    return check_match(a,b) or check_match(b,a)
