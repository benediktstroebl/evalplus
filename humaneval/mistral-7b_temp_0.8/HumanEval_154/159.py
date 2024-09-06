
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    pattern_string = []

    if len(a) > len(b):
        for i in range(len(b)):
            pattern_string.append(b[i:])
    else:
        for i in range(len(a)):
            pattern_string.append(a[i:])

    for p in pattern_string:
        if b in a:
            return True

        elif p in a:
            return True

    return False

