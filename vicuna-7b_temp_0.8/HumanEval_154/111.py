
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    n1 = len(a)
    n2 = len(b)
    for i in range(n2):
        for j in range(n1):
            if a[j] == b[i]:
                for k in range(n2):
                    if b[i] == b[k]:
                        continue
                    if b[k:k+len(b[i])] == b[i]:
                        return True
    return False
