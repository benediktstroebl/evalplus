
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    
    a = list(a)
    b = list(b)
    b_s = set(b)
    s = set()
    
    if b == a or a == b:
        return False
    
    for i in a:
        s.add(i)
    
    for j in range(len(a)):
        x = a[j:] + a[:j]
        if any(x[i:i+len(b)] == b for i in range(len(a)-len(b)+1)):
            return True
    
    return False
