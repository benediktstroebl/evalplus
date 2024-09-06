
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    i=0
    c=0
    if len(b)==0:
        return False
    for j in range(len(b)):
        if b[j]==a[i]:
            c=c+1
            i=i+1
        if c==len(b):
            return True
        if i==len(a):
            i=0
    return False



