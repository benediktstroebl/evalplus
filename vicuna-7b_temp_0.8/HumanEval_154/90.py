
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    d = len(a)
    for i in range(d):
        for j in range(i+1,d):
            for k in range(j+1,d):
                for l in range(k+1,d):
                    if (a[i:j]+a[j:k]+a[k:l]+a[l:d]) in b:
                        return True
    return False
