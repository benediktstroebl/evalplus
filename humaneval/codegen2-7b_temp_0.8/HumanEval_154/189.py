
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l=len(a)
    for i in range(0, l):
        if a[i]!= b[0]:
            continue
        else:
            if l-i <= 0 :
                return True
            else:
                if cycpattern_check(b[1:], a[i+1:]) == True:
                    return True
                else:
                    continue
    return False
