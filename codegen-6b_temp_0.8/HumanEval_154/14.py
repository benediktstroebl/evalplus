
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def in_substr(substr, word):
        return substr in word

    def is_cyclic_rotation(a,b):
        if len(a) != len(b):
            return False
        n = len(a)
        b_str = ''.join(sorted(b))
        for i in range(n):
            if a[i:] == b_str[:n-i]:
                return True
        return False

    if in_substr(b, a):
        return True
    if is_cyclic_rotation(a, b):
        return True
    return False
