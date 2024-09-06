
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(len(a)):
                if a[k] != a[j] and a[j] != a[i]+1 and a[i] != a[k]:
                    b = ""
                    for i in range(len(a)):
                        b += a[i]
                    if b.find(b[len(b)-2:]) == 0 and b.find(b[len(b)-3:]) == 0:
                        return True
    return False