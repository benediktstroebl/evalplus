
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1 = len(a)
    l2 = len(b)
    for i in range(l1):
        l = 0
        while l<l2 and a[i:i+l+1] == b[0:l+1]:
            l += 1
        if l == l2:
            return True
    return False
