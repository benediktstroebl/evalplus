
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    a = [word.lower() for word in a.split()]
    b = [word.lower() for word in b.split()]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] in b[j] or b[j] in "".join(a[i:]).lower():
                return True
    return False
