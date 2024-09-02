
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)>len(b):
        return False
    l = len(b)
    s = set()
    for i in range(l):
        s.add(b[i:(i+1)]+" "+b[(i+1)%l:(i+2)%l])
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)] in s:
            return True
    return False
