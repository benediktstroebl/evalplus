
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)!= len(b):
        return False
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    if a_sorted == b_sorted:
        return True
    for i in range(len(b)):
        if a_sorted[i]!= b_sorted[i]:
            break
    return b_sorted[i] in a_sorted[len(a):
