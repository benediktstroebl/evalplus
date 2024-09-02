
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def is_rotated(a,b):
        return a+a == b+b

    def contains_rotations(a):
        for i in range(1,len(a)):
            if is_rotated(a[i:], a[:i]):
                return True
        return False

    return contains_rotations(b)

