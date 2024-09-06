
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = sorted(a)
    b = sorted(b)
    diff = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] != b[j] and a[i] in b[j:]:
                diff += 1
        if diff == 0 and b[i] in a[j:]:
            break
    if diff == len(a) or b[i] in a[j:] or len(a[j:]) == len(b):
        return False
    for i in range(len(b)):
        for j in range(len(a)):
            if a[i] in b[j:] and b[i] in a[j:]:
                return True
    return False