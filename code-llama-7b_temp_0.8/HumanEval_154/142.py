
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a == "" and b != "":
        return False
    if b == "" and a != "":
        return False

    if len(a) == len(b):
        return False

    if len(b) > len(a):
        return False
    # print(a)
    if a.find(b) != -1:
        return True

    for i in range(len(b)):
        # print(b)
        if b.find(b[i], i+1) != -1:
            return False
        return a.find(b[(i+1)%len(b)]) != -1
        # return a.find(b[i]) != -1

    return False

