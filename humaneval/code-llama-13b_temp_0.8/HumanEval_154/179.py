
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(a == b):
        return True

    pattern = a
    size = len(pattern)
    i = 0
    while i < size:
        pattern = pattern + pattern[0]
        i += 1
    index = pattern.find(b)
    if(index != -1):
        return True
    return False
