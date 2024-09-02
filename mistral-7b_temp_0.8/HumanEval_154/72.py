
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a_list = list(a)
    b_list = list(b)
    #print(b_list)
    a_list.sort()
    b_list.sort()
    #print(b_list)
    if a_list == b_list:
        return True
    return False
