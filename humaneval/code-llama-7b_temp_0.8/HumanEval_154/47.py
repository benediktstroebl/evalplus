
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n = len(a)
    m = len(b)
    # a is the main string and b is the substring
    b = b[::-1]
    # if the length of b is not a factor of n then it is not possible to obtain b by rotating a
    if n%m != 0:
        return False
    # check each k sized rotations of a 
    for k in range(0,n,m):
        if a[k:k+m] == b:
            return True
    return False

