
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

    if len(b_list) > len(a_list):
        return False

    for i in range(len(b_list), len(a_list)):
        if a_list[i:i+len(b_list)] == b_list:
            return True

    return False
