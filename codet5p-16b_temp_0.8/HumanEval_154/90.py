
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    if len(b) == len(a):
        return (b in a)

    for i in range(len(a)):
        if a[i]!= b[0]:
            continue
        for j in range(i, len(a)):
            if a[j]!= b[0]:
                continue
            for k in range(j, len(a)):
                if a[k]!= b[0]:
                    continue
                if b in a[j:k+1]:
                    return True

    return False




