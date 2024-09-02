
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    list1 = list(a)
    list2 = list(b)
    if len(list1) != len(list2):
        return False
    if list1 == list2:
        return True
    if list1[::-1] == list2:
        return True
    if list1[::-1][1::] == list2:
        return True
    return False


