
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not a:
        return False
    return has_substring(b, a) or has_substring(b, rotate_string(a))

assert(cycpattern_check("abcd","abd") == False)
assert(cycpattern_check("hello","ell") == True)
assert(cycpattern_check("whassup","psus") == False)
assert(cycpattern_check("abab","baa") == True)
assert(cycpattern_check("efef","eeff") == False)
assert(cycpattern_check("himenss","simen") == True)

