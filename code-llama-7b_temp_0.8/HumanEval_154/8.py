
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a=a.replace(" ","")
    b=b.replace(" ","")
    #return b in a
    if b in a:
        return True
    if b == a[len(b):]:
        return True
    for i in range(1,len(b)):
        print(a[i:],b[:i])
        if a[i:] == b[:i]:
            return True
    return False


