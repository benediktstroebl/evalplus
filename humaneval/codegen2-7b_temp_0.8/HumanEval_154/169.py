
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(len(a) == len(b)):
        return True
    else:
        a_rotate = a[len(a)-len(b):] + a[0:len(a)-len(b)]
        return a_rotate in b or cycpattern_check(a_rotate,b)

















