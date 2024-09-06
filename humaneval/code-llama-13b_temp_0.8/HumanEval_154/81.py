
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #We check if b is substring of a
    if b in a:
        return True
    #We check if b is reversed substring of a
    elif b[::-1] in a:
        return True
    #We check if b is substring of a reversed
    elif b in a[::-1]:
        return True
    #We check if b is reversed substring of a reversed
    elif b[::-1] in a[::-1]:
        return True
    #If none of the above is true, then we return False
    return False
