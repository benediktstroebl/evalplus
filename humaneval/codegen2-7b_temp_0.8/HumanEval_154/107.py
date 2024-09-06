
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a==b:
        return True
    if len(a)==len(b) and a==b[::-1]:
        return True
    if len(a)>len(b):
        b=b+a[len(a)-len(b):]
    else:
        a=a+b[len(b)-len(a):]
    if a==b:
        return True
    return False
