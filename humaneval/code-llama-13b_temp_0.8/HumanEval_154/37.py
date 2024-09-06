
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)==len(b):
        return False
    else:
        for i in range(len(a)):
            for j in range(i,len(a)):
                a1=a[i:j+1]
                if len(a1)==len(b):
                    if a1==b:
                        return True
                for k in range(len(b)):
                    for l in range(k,len(b)):
                        b1=b[k:l+1]
                        if len(a1)==len(b1):
                            if a1==b1:
                                return True
    return False

