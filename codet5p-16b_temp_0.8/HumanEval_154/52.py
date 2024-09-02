
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    l1 = list(a)
    l2 = list(b)
    for i in range(len(l1)):
        if l1.count(l1[i]) >= l2.count(l1[i]) or l2.count(l1[i]) >= l1.count(l1[i]):
            return True
    return False




