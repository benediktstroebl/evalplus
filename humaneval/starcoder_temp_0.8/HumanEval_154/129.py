
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if len(a) == 0 or len(b) == 0:
        return False

    if len(b) == 1:
        return True

    b_rotated = b[1:] + b[0]

    # O(b^2)
    for i in range(len(a) - len(b) + 1):
        if a[i : i + len(b)] == b or a[i : i + len(b)] == b_rotated:
            return True

    return False
