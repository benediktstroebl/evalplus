
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    
    print("cycpattern_check({},{})".format(a,b))
    n = len(a)
    for i in range(0,n):
        if b == a[i:n]+a[0:i]:
            print("True")
            return True
    print("False")
    return False
