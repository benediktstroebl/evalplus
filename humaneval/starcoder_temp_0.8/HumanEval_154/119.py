
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    len_a = len(a)
    len_b = len(b)

    # Check length
    if len_a <= len_b:
        return False

    # Check if substring is in a
    for i in range(len_a - len_b + 1):
        if a[i:i + len_b] == b:
            return True
    return False

