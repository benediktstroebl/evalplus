
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False

    """
    The easiest way to check if one string is a substring of another is to use the `in` operator.
    The other way to check if one string is a substring of another is to use the `startswith` and `endswith` operators.
    """
    return b in a + a[::-1]

