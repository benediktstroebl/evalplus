
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """


    #TODO: Write your code here
    if(b in a):
        return True
    else:
        l = len(b)
        r = len(a)
        if(l > r):
            return False
        else:
            for i in range(l):
                if(a[i: l+i] == b):
                    return True
            return False
