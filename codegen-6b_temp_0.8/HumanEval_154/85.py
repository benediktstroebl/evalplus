
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #without the spaces:
    if len(a) != len(b): return False
    if len(a) == 1: return False
    if len(a) == 0: return True
    patterns = [a]
    for _ in range(len(a)):
        patterns += [b[-1] + b[:-1], b[1:] + b[:-1], b[-1] + b[1:], b[:-1] + b[1:]]

    return any(all(i in x for x in patterns) for i in b)

