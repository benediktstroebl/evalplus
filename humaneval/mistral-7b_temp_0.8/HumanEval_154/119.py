
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(a) - len(b)):
        if a[i:i + len(b)] == b:
            return True
        elif a[i + 1:i + len(b) + 1] == b:
            return True
        elif a[i + 2:i + len(b) + 2] == b:
            return True
        elif a[i + 3:i + len(b) + 3] == b:
            return True
        elif a[i + 4:i + len(b) + 4] == b:
            return True

    return False
