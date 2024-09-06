
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    d = {}
    for word in a:
        d[word] = 1
    for word in b:
        if word in d:
            return True
        elif d.get(word[::-1]) == 1:
            return True
        else:
            d[word] = 1
            d[word[::-1]] = 1
    return False

