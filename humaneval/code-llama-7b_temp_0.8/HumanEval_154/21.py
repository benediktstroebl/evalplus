
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    b=b[::-1]
    lena=len(a)
    lenb=len(b)
    if lenb>lena:
        return False
    if lena%lenb!=0:
        return False
    for i in range(0,lena,lenb):
        if a[i:i+lenb]==b:
            return True
    return False

