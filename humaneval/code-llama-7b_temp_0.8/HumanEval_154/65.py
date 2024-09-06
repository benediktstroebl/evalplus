
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    temp = []
    if len(a) == len(b):
        return False

    if len(b) > len(a):
        a , b = b , a
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True

    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                temp.append(a[i:]+a[:i])
    for i in range(len(temp)):
        if temp[i] == b:
            return True

    return False

