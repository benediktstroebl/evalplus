
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def cycpattern_check_helper(a , b):
        if a == "":
            return True
        if b == "":
            return False
        if a[0] == b[0]:
            return cycpattern_check_helper(a[1:], b[1:])
        return cycpattern_check_helper(a[1:], b) or cycpattern_check_helper(a, b[1:])

    return cycpattern_check_helper(a,b)

