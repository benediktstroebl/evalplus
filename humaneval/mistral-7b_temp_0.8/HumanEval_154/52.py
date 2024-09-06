
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    s1 = set(a)
    s2 = set(b)
    if len(s1) > len(s2):
        return False

    else:
        flag = 0
        for i in s2:
            if i in s1:
                flag += 1
        if flag == len(s2):
            return True
        else:
            return False




