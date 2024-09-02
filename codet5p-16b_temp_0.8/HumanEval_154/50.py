
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    c1 = b + b
    c2 = b + b + b
    c3 = c1[1:len(b)]
    c4 = c2[1:len(b)]
    c5 = c3[1:len(b)]
    c6 = c4[1:len(b)]
    c7 = c5[1:len(b)]
    c8 = c6[1:len(b)]

    if any(c1 in a for c1 in [c1,c2,c3,c4,c5,c6,c7,c8]):
        return True
    else:
        return False

