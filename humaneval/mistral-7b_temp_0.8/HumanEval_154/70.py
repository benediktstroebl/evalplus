
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    # check if a is empty or not
    if len(a) == 0:
        return False

    # check if b is empty or not
    if len(b) == 0:
        return False

    # check if b is a substring of a
    if b in a:
        return True

    # check if b is a substring of a after rotating the word
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i:j+1] in a:
                return True

    return False
