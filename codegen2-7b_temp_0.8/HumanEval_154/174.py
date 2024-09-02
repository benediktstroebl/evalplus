
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    flag = 0
    for i in range(0, len(a) - 1):
        if a[i + 1:] == b:
            flag += 1
        if a[0:len(a) - i - 2] == b:
            flag += 1
    if flag > 1:
        return True
    else:
        
