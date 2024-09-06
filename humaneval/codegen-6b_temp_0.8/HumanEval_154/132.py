
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def is_rotated(s1,s2):
        return s2 in s1+s1

    #Find pattern
    def find_pattern(word):
        for i in range(len(word)):
            if is_rotated(word[i:],word[i:]):
                return word[i:]
        return None

    pattern = find_pattern(a)
    if pattern is None:
        return False
    if is_rotated(b,pattern):
        return True
    return False

