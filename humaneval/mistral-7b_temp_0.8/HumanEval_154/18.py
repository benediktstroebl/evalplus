
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    import re
    for _ in range(len(a)):
        if re.search(b,a) or re.search(a,b) or re.search(b[::-1],a) or re.search(a[::-1],b) or re.search(b[1:],a) or re.search(a[1:],b):
            return True
        else:
            return False
    return "None"
