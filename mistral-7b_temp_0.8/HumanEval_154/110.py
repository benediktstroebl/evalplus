
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) < len(b):
        b = b[1:] + b[:1]
    a_list = list(a)
    b_list = list(b)
    if len(a_list) == len(b_list):
        for i in range(len(a_list)):
            if a_list[i] != b_list[i]:
                return False
        return True
    else:
        return False
