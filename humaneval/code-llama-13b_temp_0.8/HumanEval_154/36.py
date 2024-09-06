
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    length = len(b)

    if length > len(a):
        return False

    if length == len(a) and a == b:
        return True

    if a.find(b) != -1:
        return True

    for i in range(0, length):
        if a.find(b[0:length-1] + b[i] + b[1:length]) != -1:
            return True

    return False
