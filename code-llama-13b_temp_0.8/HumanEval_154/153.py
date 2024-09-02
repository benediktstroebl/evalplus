
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
    s1=a
    s2=b
    l1=len(s1)
    l2=len(s2)
    for i in range(l2):
        a=s1.find(s2)
        if(a!=-1):
            return True
        else:
            b=s2[-1]
            s2=s2[1:]+b
    return False

