
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a=a.lower()
    b=b.lower()
    for x in range(1,len(b)):
        # b=b[0:x]
        b1=b[x:]+b[:x]
        # print(b1)
        if b1 in a:
            return True
    return False
