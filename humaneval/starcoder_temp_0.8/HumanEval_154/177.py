
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    i = len(a)
    j = len(b)
    if j > i:
        return False

    if j == 0:
        return True

    if i == j:
        return a == b

    # i > j
    for k in range(1, i + 1):
        flag = 0
        if k == j:
            flag = 1
        if b == a[i - k:i] or flag == 1:
            return True

    return False

