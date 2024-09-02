
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # code goes here
    l1=len(a)
    l2=len(b)
    if(l1>l2):
        for i in range(l1-l2):
            temp=a[i:i+l2]
            if(b==temp):
                return True
    return False

