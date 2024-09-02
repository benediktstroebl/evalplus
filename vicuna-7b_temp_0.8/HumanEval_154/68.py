
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = a.lower()
    b = b.lower()
    if a == b:
        return False
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            rot_a = a[i:j] + a[j:i+1]
            if rot_a in b:
                return True
    return False
