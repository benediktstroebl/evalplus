
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    l = len(a)
    dic = {}
    for i in range(1, l+1):
        dic[a[(l-i):l]] = 1
    if b in dic:
        return True
    elif b in dic.values():
        return False
    else:
        return False
