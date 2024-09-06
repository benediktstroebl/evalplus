
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # your code goes here
    n = len(a)
    k = len(b)
    
    if k > n:
        return False
    
    for i in range(n-k+1):
        l = a[i:i+k]
        if l == b or l == b[::-1]:
            return True
    return False
    
