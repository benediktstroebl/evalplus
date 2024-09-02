
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not b:
        return False
    if not a:
        return False
    # when the length of the second word is not in the first word return False
    if len(b) not in list(range(len(a))):
        return False

    # compare b to a and return True if found
    if b in a:
        return True

    # when b not in a
    else:
        # loop over the len of b
        for i in range(len(b)):
            # rotate b by one and check if rotated b is a substring in a
            if b[i:] + b[:i] in a:
                return True

        # when the above checks failed return False
        return False
