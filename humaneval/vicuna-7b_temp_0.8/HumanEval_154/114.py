
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if a == b:
        return True
    for i in range(len(b)):
        if b[i] in a or a[i] in b or a[i] == b[i] + "":
            if cycpattern_check(a, b[0:i]+b[i+1:]) or cycpattern_check(a, b[0:i] + b[i+1:]):
                return True
    return False
