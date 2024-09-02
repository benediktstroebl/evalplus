
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n1 = len(a)
    n2 = len(b)
    i1 = j1 = 0
    i2 = j2 = n2
    while j2 >= 0:
        if b[j2] == a[i1]:
            i1 += 1
            j1 += 1
            if j1 >= n1:
                break
        j2 -= 1
    while j1 < n1:
        if b[j1] == a[i2]:
            i2 -= 1
            j1 += 1
            if j1 >= n1:
                break
        j1 += 1
    return i1 > 0 or i2 > 0