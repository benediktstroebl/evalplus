
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if a.lower().find(b.lower())!= -1: #if the second word is a substring in the first word
        return True
    else:
        for x in range(len(b)): #if the second word can be found by rotating the first word, return True
            if b[x:]+b[:x] == a:
                return True
    return False

