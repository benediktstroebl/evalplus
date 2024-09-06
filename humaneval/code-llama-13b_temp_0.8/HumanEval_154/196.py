
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) > len(a):
        return False
    
    p = [0] * len(b)
    
    for i in range(len(b) - 1):
        if b[i + 1] == b[i]:
            p[i + 1] = p[i] + 1
    
    j = 0
    for i in range(len(a)):
        while j > 0 and a[i] != b[j]:
            j = p[j - 1]
        if a[i] == b[j]:
            j += 1
        if j == len(b):
            return True
    return False




    
    
