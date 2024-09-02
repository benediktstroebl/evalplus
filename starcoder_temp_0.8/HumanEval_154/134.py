
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #Your code here
    i = 0
    j = 0
    while(i < len(a) and j < len(b)):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(b):
        return True
    else:
        return False
