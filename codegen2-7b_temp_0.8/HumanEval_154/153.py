
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

    a_index = 0
    for i in range(len(a)):
        if a[a_index] == b[i]:
            a_index += 1

        if a_index == len(b):
            return True

    return a_index == len(b)
