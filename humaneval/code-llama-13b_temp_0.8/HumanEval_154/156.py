
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b)>len(a):
        return False
    if len(b)==len(a):
        return b in a
    l1 = []
    l2 = []
    for i in range(len(b)):
        l1.append(a[i])
    for i in range(len(b)):
        l1.append(a[i])
    for i in range(len(b)):
        l2.append(b[i])
    if l2 == l1:
        return True
    else:
        for i in range(len(b)-1):
            l2.insert(0,l2[-1])
            l2.pop()
            if l2 == l1:
                return True
        return False
        
    
