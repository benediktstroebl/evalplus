
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    dp=0
    for i in range(len(a)):
        dp += a[i:].count(a[i:i+1] + a[i+1:])
    for i in range(len(b)):
        if b[i:].count(b[i:i+1] + b[i+1:]) or any(map(lambda x:x.count(x[i:i+1] + x[i+1:]),b[i:].split())):
            return True
        dp += b[i:].count(b[i:i+1] + b[i+1:])
    return dp == len(a)
