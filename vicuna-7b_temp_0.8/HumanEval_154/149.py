
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        if b[i] not in a:
            return False
        for j in range(len(b)):
            if (i,j) in [(i+x, j+y) for x, y in [(1,0),(-1,0)]]:
                #perform rotations
                b = b[::-1]
            if b[i:j] in a:
                return True
    return False
