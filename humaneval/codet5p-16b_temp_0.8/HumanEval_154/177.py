
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_temp = a
    b_temp = b
    for i in range(len(a)):
        if a_temp == b_temp:
            return True
        else:
            a_temp = a_temp[1:] + a_temp[0]
            if a_temp == b_temp:
                return True
            b_temp = b_temp[1:] + b_temp[0]
    return False

