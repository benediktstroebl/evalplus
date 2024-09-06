
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    import string
    import re
    a=a.lower()
    b=b.lower()
    #print(a,b)
    if b in a:
        return True
    for c in string.ascii_lowercase:
        if re.findall(c+'.*'+b,a):
            return True
    return False

