
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    try:
        n = len(a)
        m = len(b)
        if m>n:
            return False
        for i in range(n):
            for j in range(m):
                if a[i] != b[j]:
                    break
                elif j == m-1:
                    return True
                else:
                    continue
        return False
    except:
        return False
