
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def isSubstring(a,b,i):
        if a[i:i+len(b)] == b:
            return True
        return False
    for i in range(len(a)):
        if isSubstring(a,b,i):
            return True
        for j in range(len(b)):
            if isSubstring(a,b,i + j):
                return True
    return False
