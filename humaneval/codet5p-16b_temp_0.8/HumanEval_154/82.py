
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a=a.lower()
    b=b.lower()

    if len(a) == len(b):
        pass
    else:
        return False

    if b in a or a in b:
        return True

    a_rotations = []
    for i in range(len(a)):
        a_rotations.append(a[i:]+a[:i])


    return any([True for i in a_rotations if b in i])


