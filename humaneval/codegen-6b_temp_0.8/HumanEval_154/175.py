
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    s1, s2 = a, b
    for i in range(len(a)):
        if s1 == s2:
            return True
        elif s1 == s2[1:] + s2[0]:
            return True
        elif s2 == s1[1:] + s1[0]:
            return True
        else:
            continue

    return False

