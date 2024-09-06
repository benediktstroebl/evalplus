
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        return False
    for c in b[1:]:
        if a.startswith(c):
            return True
    for i in range(1, len(b)):
        for j in range(i+1, len(b)):
            if b[j] != b[i+1]:
                break
        if a.startswith(b[i:j+1]) or a.startswith(b[j+1:]) or a.startswith(b[i:j+1]):
            return True
    return False