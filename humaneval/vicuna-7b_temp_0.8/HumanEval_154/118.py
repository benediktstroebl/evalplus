
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for c in b:
        if b.count(c) > a.count(c):
            return True
        for i in range(1, len(b)):
            for j in range(i, len(b)):
                temp = b[i:j]
                if temp in a:
                    return True
    return False