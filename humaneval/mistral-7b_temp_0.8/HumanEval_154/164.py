
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1=len(a)
    l2=len(b)
    if l2 > l1:
        return False
    elif l2 == l1:
        return True
    else:
        for i in range(l1-l2+1):
            if a[i:i+l2]==b:
                return True
        else:
            return False


